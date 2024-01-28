import json
from multiprocessing import Queue
from threading import Thread

import pandas as pd

from tests.databricks.db_test_utils import *
from tests.databricks.db_test_utils import (
    run_endpoint_tests,
    get_or_create_test_cluster,
    subtester_thread,
)
from tmp.db_marketplace.generate_job_payload import (
    generate_payloads,
    models_uploaded,
    titles_in_marketplace,
)
from tmp.db_marketplace.generate_nb import generate_notebook


def log_and_get_failed_models(results):
    retry_models = []
    for model, result in results.items():
        print(f"Model {model}: {result}")
        if result["success"] is False:
            retry_models.append(model)
    return retry_models


def parallel_run(
    cluster_ids,
    n_parallel_jobs_per_cluster,
    models_to_test,
    host,
    token,
    results,
    test_type,
):
    # 3) For each cluster, start a tester-thread.
    # Start an extra thread for same cluster, for every parallel job run on cluster
    # Threads take jobs from the queue and run them on the cluster till completion.
    job_que = Queue()
    for model in models_to_test:
        job_que.put(model)
    threads = []
    for cluster_id in cluster_ids:
        for i in range(n_parallel_jobs_per_cluster):
            # Start 1 thread for every job that should run, for every cluster
            t = Thread(
                target=subtester_thread,
                args=(
                    cluster_id,
                    job_que,
                    host,
                    token,
                    results,
                    test_type,
                ),
            )
            threads.append(t)
            t.start()
    # Wait for all threads to finish
    for t in threads:
        t.join()


# @pytest.mark.skip(reason="WIP")
@db_cloud_node_params
def test_endpoints_multi_cluster(creds, node_type):
    n_clusters = 1
    n_parallel_jobs_per_cluster = 2
    runtime = "9.1.x-scala2.12"
    lic, host, token = creds

    # 1) Create clusters
    cluster_ids = [
        get_or_create_test_cluster(creds, node_type, i, runtime=runtime)
        for i in range(n_clusters)
    ]

    # 2) Define models to test
    models_to_test = get_mm_models()  # [:3]
    models_to_test = ["tokenize"]
    # one_model_per_class = get_one_model_per_class()

    # 3) Start parallel-job-cluster test
    results = {}
    # test_type = "load_predict"  # 'endpoint'
    test_type = "endpoint"  # ''
    parallel_run(
        cluster_ids=cluster_ids,
        n_parallel_jobs_per_cluster=n_parallel_jobs_per_cluster,
        models_to_test=models_to_test,
        host=host,
        token=token,
        results=results,
        test_type=test_type,
    )

    retry_models = log_and_get_failed_models(results)
    print(f"Retrying {len(retry_models)} models")
    # Give clusters some time to recover from any failures
    time.sleep(60 * 5)

    # run failed models again, with job-parallelism 1 but same cluster-parallelism
    parallel_run(
        cluster_ids=cluster_ids,
        n_parallel_jobs_per_cluster=1,
        models_to_test=retry_models,
        host=host,
        token=token,
        results=results,
        test_type=test_type,
    )
    json.dump(results, open("results.json", "w"))

    # 5) Delete all clusters
    # for cluster_id in cluster_ids:
    #     delete_cluster(cluster_id)


@db_cloud_node_params
def test_endpoint(creds, node_type):
    lic, host, token = creds
    # runtime = "13.3.x-cpu-ml-scala2.12" # ML runtime
    # runtime = "12.2.x-gpu-ml-scala2.12"
    cluster_id = get_or_create_test_cluster(
        creds,
        node_type,
        1,
        clean_workspace=True,  # runtime=runtime
    )
    job_url, success = run_endpoint_tests(cluster_id, host, token, "tokenize")
    assert success


@db_marketplace_cloud_node_params
def test_endpoint_publish_list(creds, node_type):
    # runtime = "13.3.x-cpu-ml-scala2.12" # ML runtime
    # runtime = "12.2.x-gpu-ml-scala2.12"
    lic, host, token = creds
    df = pd.read_excel(
        "/home/ckl/data-server/backup_popos_workstation_2023/Documents/freelance/jsl/johnsnowlabs-4-real/tests/FINAL_MODEL_LIST.xlsx",
        sheet_name="top_60_pipeline",
    )

    # 1. generate a payload for every model submission
    payloads = generate_payloads(df)
    # print("payloads", payloads)
    cluster_id = get_or_create_test_cluster(
        creds,
        node_type,
        8,
        clean_workspace=True,  # runtime=runtime
        runtime="12.2.x-scala2.12",  # needs unity catalog!
    )
    nb_p = "/home/ckl/data-server/backup_popos_workstation_2023/freelance/jsl/johnsnowlabs-4-real/tmp/db_marketplace/mmm_upload5.ipynb"
    lic, host, token = creds
    total = len(payloads)
    for i, p in enumerate(payloads):
        print(f"Submitting {i}/{total}: {p['nlu_ref']}")
        nlp.run_in_databricks(
            nb_p,
            cluster_id,
            run_name=f"auto_run1_{p['nlu_ref']}",
            dst_path="/Users/christian@johnsnowlabs.com/test5.ipynb",
            databricks_token=token,
            databricks_host=host,
            parameters={
                "nlu_ref": p["nlu_ref"],
                # "nlu_ref": "tokenize",
                "listing_title": p["pipe_name"],
                "listing_short_description": p["short_description"],
                "listing_long_description": p["long_description"],
                "release_id": "0.9",
                "proivider_folder": "johnsnowlabs_folder",
            },
        )
    # job_url, success = run_endpoint_publish_tests(cluster_id, host, token, "tokenize")
    # assert success


@db_marketplace_cloud_node_params
def test_endpoint_publish_missing(creds, node_type):
    # runtime = "13.3.x-cpu-ml-scala2.12" # ML runtime
    # runtime = "12.2.x-gpu-ml-scala2.12"
    node_type = "r5d.4xlarge"
    lic, host, token = creds
    df = pd.read_excel(
        "/home/ckl/data-server/backup_popos_workstation_2023/Documents/freelance/jsl/johnsnowlabs-4-real/tests/FINAL_MODEL_LIST.xlsx",
        sheet_name="top_60_pipeline",
    )
    uploaded_models = pd.DataFrame(models_uploaded).reset_index()

    # 1. generate a payload for every model submission
    payloads = generate_payloads(df, uploaded_models)
    # print("payloads", payloads)
    cluster_id = get_or_create_test_cluster(
        creds,
        node_type,
        13,
        clean_workspace=True,  # runtime=runtime
        runtime="12.2.x-scala2.12",  # needs unity catalog!
    )
    nb_p = "/home/ckl/data-server/backup_popos_workstation_2023/Documents/freelance/jsl/johnsnowlabs-4-real/tmp/db_marketplace/mmm_upload1.ipynb"
    lic, host, token = creds
    total = len(payloads)
    for i, p in enumerate(payloads):
        print(f"Submitting {i}/{total}: {p['nlu_ref']}")
        # if (
        #     # "en.ner.oncology.pipeline en.assert.oncology_wip en.relation.oncology_biobert_wip"
        #     "en.map_entity.rxnorm_resolver.pipe"
        #     != p["nlu_ref"]
        # ):
        #     print("Skipping", p["nlu_ref"])
        #     continue
        nlp.run_in_databricks(
            nb_p,
            cluster_id,
            run_name=f"auto_run1_{p['nlu_ref']}",
            dst_path="/Users/christian@johnsnowlabs.com/test1.ipynb",
            databricks_token=token,
            databricks_host=host,
            parameters={
                "nlu_ref": p["nlu_ref"],
                # "nlu_ref": "tokenize",
                "listing_title": p["pipe_name"],
                "listing_short_description": p["short_description"],
                "listing_long_description": p["long_description"],
                "release_id": "0.9",
                "proivider_folder": "johnsnowlabs_folder",
            },
        )


@db_marketplace_cloud_node_params
def test_endpoint_publish_single(creds, node_type):
    lic, host, token = creds
    payloads = []
    # runtime = "13.3.x-cpu-ml-scala2.12" # ML runtime
    # runtime = "12.2.x-gpu-ml-scala2.12"
    cluster_id = get_or_create_test_cluster(
        creds,
        node_type,
        6,
        clean_workspace=False,
        runtime="12.2.x-scala2.12",  # needs unity catalog!
        # And mlflow version with random hakcy hacky?!
    )
    job_url, success = run_endpoint_publish_tests(cluster_id, host, token, "tokenize")
    assert success


@db_cloud_node_params
def test_endpoint_licensed(creds, node_type):
    lic, host, token = creds
    cluster_id = get_or_create_test_cluster(creds, node_type, 3, clean_workspace=True)
    job_url, success = run_endpoint_tests(
        cluster_id, host, token, "en.med_ner.clinical"
    )

    assert success

    nlp.install()


def test_endpoint_consumer():
    # Use consumer notebook, paramterize with creds!
    pass


"""
We want to be able to test on :  
- List of models
- List of runtimes
- auto-generate benchmarks --> time for load/predicting

# TODO
- handle spot instance reclamation https://dbc-3d4c44aa-a512.cloud.databricks.com/?o=4085846932608579#job/407841450144996/run/583312836892114 -162028-g0yy9b85
- handle endpoint stuck/ use timeout 60mins 


"""


# https://github.com/qdrant/qdrant-haystack/tree/master


def test_find_miss_models():
    p = "/home/ckl/data-server/backup_popos_workstation_2023/Documents/freelance/jsl/johnsnowlabs-4-real/tests/FINAL_MODEL_LIST.xlsx"
    # p = "/home/ckl/data-server/backup_popos_workstation_2023/Documents/freelance/jsl/johnsnowlabs-4-real/tests/FINAL_MODEL_LIST.xlsx"

    jsl_offer_df = pd.read_excel(
        p,
        sheet_name="top_60_pipeline",
    )
    models_in_marketplaces = titles_in_marketplace
    uploaded_models = pd.DataFrame(models_uploaded).reset_index()
    in_excel_but_not_market = []
    missing_release_table_nlu_ref = []
    missing_release_table_title = []

    # In marketplace but not release Table
    for i, row in uploaded_models.iterrows():
        if row["Title"] not in models_in_marketplaces:
            missing_release_table_nlu_ref.append(row["NluRef"])
            missing_release_table_title.append(row["Title"])

    # In excel but not in  Release Table
    for i, row in jsl_offer_df.iterrows():
        if not isinstance(row["Include as DB Serve Listing"], str):
            print(row)
            continue
        if row["Include as DB Serve Listing"].lower() != "yes":
            continue

        if not isinstance(row["nlu_ref"], str):
            continue

        if row["nlu_ref"].strip() not in uploaded_models["NluRef"].values:
            in_excel_but_not_market.append(row["nlu_ref"].strip())
    print(in_excel_but_not_market)

    uploaded_models = pd.DataFrame(models_uploaded).reset_index()

    # Get all payloads we would send
    payloads = generate_payloads(jsl_offer_df, uploaded_models)
    print("Total payloads", len(payloads))
    for p in payloads:
        print(p["nlu_ref"])


def test_get_ok():
    jsl_offer_df = pd.read_excel(
        "/home/ckl/data-server/backup_popos_workstation_2023/Documents/freelance/jsl/johnsnowlabs-4-real/tests/FINAL_MODEL_LIST.xlsx",
        sheet_name="top_60_pipeline",
    )
    r = []
    for idx, row in jsl_offer_df.iterrows():
        if row["Include as DB Serve Listing"] == "Yes":
            # if not isinstance(row["nlu_ref"], str):
            #     continue
            r.append(row)
    print(len(r))
    for l in r:
        print(l["nlu_ref"], "+", l["Pipeline Name"])

    refs = []


"""
1. LP Bug  Make sure such annotators exist in your pipeline, with the right output names and that they have following annotator types: chunk
    - en.snomed.umls.mapping
    - en.map_entity.snomed_to_icd10cm.pipe
    -  en.map_entity.snomed_to_icd10cm.pipe

2. Broken TF Graph: No Operation named [save/restore_all] in the Graph
    - en.summarize.clinical_questions.pipeline

3. \n in name? 
    - en.summarize.biomedical_pubmed.pipeline
 
4. OOM? 
 -  en.summarize.clinical_jsl_augmented.pipeline
 
 
5. Dafuq DB bug? RestException: INVALID_PARAMETER_VALUE: CreateRegisteredModel name is not a valid name
   - en.ner.oncology.pipeline en.assert.oncology_wip en.relation.oncology_biobert_wip
     - only once Also WTF Tripple NLU ref?!??!(Extract oncological entities and relations)
   - en.med_ner.vop.pipeline

6. Bad path on dbfs? org.apache.hadoop.mapred.InvalidInputException: Input path does not exist: /root/cache_pretrained/umls_drug_resolver_pipeline_en_4.4.4_3.2_1687528338674/metadata
    - en.map_entity.umls_drug_resolver

7. Missing Relation key in extract KeyError: 'relation'
    - en.map_entity.rxnorm_resolver.pipe
    - en.icd10cm_resolver.pipeline


nan Summarize Clinical Notes in Laymen Terms --> Need to create? 
nan Medical Question Answering (Open-Book on Clinical Notes) --> Need to create?  


ADD TO SPELLBOOK en.rxnorm.mes.mapping?!

"""


def test_gen_nb(creds, node_type):
    jsl_offer_df = pd.read_excel(
        "/home/ckl/data-server/backup_popos_workstation_2023/Documents/freelance/jsl/johnsnowlabs-4-real/tests/FINAL_MODEL_LIST.xlsx",
        sheet_name="top_60_pipeline",
    )
    for p in generate_payloads(jsl_offer_df):
        pass


@db_cloud_node_params
def test_nb_gen_on_db(creds, node_type):
    # runtime = "13.3.x-cpu-ml-scala2.12" # ML runtime
    # runtime = "12.2.x-gpu-ml-scala2.12"
    lic, host, token = creds
    df = pd.read_excel(
        "/home/ckl/data-server/backup_popos_workstation_2023/Documents/freelance/jsl/johnsnowlabs-4-real/tests/FINAL_MODEL_LIST.xlsx",
        sheet_name="top_60_pipeline",
    )
    payloads = generate_payloads(df)
    # print("payloads", payloads)
    cluster_id = get_or_create_test_cluster(
        creds,
        node_type,
        3,
        clean_workspace=True,  # runtime=runtime
        runtime="12.2.x-scala2.12",  # needs unity catalog!
    )
    lic, host, token = creds
    total = len(payloads)
    for i, p in enumerate(payloads):
        nb_p = generate_notebook(p)
        print(f"Submitting {i}/{total}: {p['nlu_ref'] + p['pipe_name']}")
        name = nb_p.split("/")[-1].replace(".ipynb", "")

        nlp.run_in_databricks(
            nb_p,
            cluster_id,
            run_name=f"auto_run1_{p['nlu_ref']}",
            dst_path=f"/Users/christian@johnsnowlabs.com/{name}.ipynb",
            databricks_token=token,
            databricks_host=host,
            parameters={
                "Databricks access token": "dapie9d02d1eb8e7ff0c4582990e2fc3b7f4",
                "Databricks host": "https://dbc-3d4c44aa-a512.cloud.databricks.com",
                "JSL-JSON-License": '{"SPARK_NLP_LICENSE": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjkyMDk1OTksImlhdCI6MTY5NzU4NzIwMCwidW5pcXVlX2lkIjoiNzc4NjI1ODgtNmQ3OS0xMWVlLTllOTMtNmEwMjc2MGNkZDQwIiwic2NvcGUiOlsiaGVhbHRoY2FyZTp0cmFpbmluZyIsImhlYWx0aGNhcmU6aW5mZXJlbmNlIl0sInBsYXRmb3JtIjp7Im5hbWUiOiJQQVlHIiwibWF4X3BhcmFsbGVsX2pvYnMiOi0xfX0.FFjHJOd7ng70SuIZ1cgO4_Ozvfk8qZUoqBw7ItdZHu2sDqP-ah5tA5SbscPsdo3x06pMW5wSoNVDwRG5CcqJWt0xlIuy3rBpwJ7ynBMYheLMvk_Uz_v-N5-Z1ngau-QeHSrGkFQsYKnPWWeeb8W-w35oDIG0vOBf4dpmwT9O6Cngloly5sSO_xHCzaShKKWFYreteC6lXVNlqJD3r5X-E0PgSMFpRlfDHtaoqHKbcyWlA1ydwR1MQCwd3i-gjfVJHArOIyvhKKrsCO6XYx_3AqG57KTrIb9FMAhLq3Z7mBEMJCvK1WUi2SbHXF0tFGdXfVUxymghcVGNYkJOlmCejw", "SECRET": "5.2.1-ffc2b401994dc1c54ff36dc6e6557a8763900a80", "JSL_VERSION": "5.2.1", "PUBLIC_VERSION": "5.2.2", "AWS_ACCESS_KEY_ID": "ASIASRWSDKBGJ2W6XEOI", "AWS_SECRET_ACCESS_KEY": "0D+RWt1ouMpe++UY+XfoD9TZKp3UsMWjiny5EHze", "AWS_SESSION_TOKEN": "IQoJb3JpZ2luX2VjEOX//////////wEaCXVzLWVhc3QtMSJIMEYCIQCXkPKBZnU/S/s4KE9W3we3cJ3TUgxuHXYFtMxt6ywv/wIhANcLt2hzmrhEABr2JRncwRQ0syJSXEUlz9HDnmE0gREqKsgCCJ7//////////wEQBBoMMTc1NDYwNTM2Mzk2IgxuXAZ4oA+QSo0BMBAqnALA5Bbnm6gseWWS5Dw2JPnpCWwiuVk5gY0EeEuanZdGdENscthnQUSoUYzphEyCNyXo05+8dtth9tbpYmwhe+mPonXDxomtSBQXmB5lxNjTT2/m0E5jqFrssJCQYNbkyF8G++6Kf0T1j2S4lMxZNaK5/BcgIBU8yas6raykF3zJQJ7khFRruwOOmTfKZlf+Mr7vxUIYfnYBmqmUffqB+syqaMetasijkxSupMFOEW8F2vNk9mRhZCq9TJ/kq4ezdVdVmRnXWKbMfHo4FNUzho00SXZaXwg23bn3PSkNSpYmGE6RwnAaWFxmC6EP0JwuzoWff8zOqjdg2Q1uqIVOTwXT10qkmU+Pz11Xvee2pGoHDauWVXymNy+UaFGFwjCA9sytBjrVAUpRH2HlKGnQi5NnmhvEu/VzhbICy9h4OsrX557m+wOiz71hGxYwVPbOAobjn6MDHSWgfXCvAyZMNvJFf0/WpoG9sLvXnYoCrRv9IJqAEtdYuNS4mof/T8YanXyeSuKikkYq046dyWgackVWQmR9GKSwvDDRrUoTVrTwQJ65ztPknsgsONHWm4h1GvHPKzWJQ1vUqxrcrI0dZI2oDeg+J3qDeaKRVnB4UioI+MSXupgnTU0yEX1ZIFI8v5tiksihI5U3khkIqII4gMTpESeX34Ub6gs2OQ=="}',
                "The model": "dropdown_id",
                "hardware_target": "CPU",
            },
        )
        break
