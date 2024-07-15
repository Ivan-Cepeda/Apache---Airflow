from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

#Aquí definimos la función que python debe ejecutar
def print_hello():
    print("Hola, este es una función para un print")

with DAG(dag_id="pythonoperator",
         description="Nuestro primer DAG utilizando Python Operator",
         schedule_interval="@once",
         start_date=datetime(2022, 8, 1)) as dag:
    
    t1 = PythonOperator(task_id="hello_with_python",
                        python_callable=print_hello)
    t1