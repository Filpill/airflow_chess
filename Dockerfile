FROM apache/airflow:3.0.3-python3.12
RUN pip install dbt dbt-bigquery
