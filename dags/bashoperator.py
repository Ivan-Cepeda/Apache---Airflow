from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(dag_id="bashoperator",
         description="Utilizando bash operator",
         start_date=datetime(2024, 7, 12),
         schedule_interval="@once") as dag:
    
    t1= BashOperator(task_id="hello-world",
                     bash_command="echo 'Hola Estoy Corriendo'")
    t1