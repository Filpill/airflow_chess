# Airflow - Orchestrating dbt Chess Transformations

The purpose of this repo is to provide a platform for learning how to deploy Airflow DAGs whilst emulating a production-like environment.

The chess transformation pipeline is constructed with dbt models: https://github.com/Filpill/dbt_chess

## DAG setup
The minimal setup we are creating is as follows:

<p align = center>
    <img src="https://github.com/Filpill/airflow_chess/blob/main/diagrams/airflow_diagram.excalidraw.png " alt="drawing" width="800"/>
</p>

- Each time the DAG is triggered, we will clone the latest version of the **dbt_chess** repo
- A dbt run is executed to the target dataset using the relevant dbt connection profile

## Dockerfile Additions
- Adding dbt library and google cloud library via pip install

## Key Additions
- Mounting service account key with permissions to interact with GCP BigQuery
