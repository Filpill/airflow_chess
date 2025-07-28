FROM apache/airflow:3.0.3-python3.12
RUN git clone https://github.com/Filpill/dbt_chess /opt/airflow/dbt
RUN pip install dbt dbt-bigquery
