from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG("dbt_chess_dag", schedule="0 11 5 * *", catchup=False) as dag:

    clone_repo = BashOperator(
        task_id="clone_repo",
        bash_command="rm -rf /tmp/dbt && git clone https://github.com/Filpill/dbt_chess.git /tmp/dbt"
    )

    run_dbt = BashOperator(
        task_id="run_dbt",
        bash_command="cd /tmp/dbt && dbt run --profiles-dir . --target airflow",
    )

    clone_repo >> run_dbt
