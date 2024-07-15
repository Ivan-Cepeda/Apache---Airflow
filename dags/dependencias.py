from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

#Aquí definimos la función que python debe ejecutar
def print_mensaje():
    print("Hola, soy tarea 1")

with DAG(dag_id="dependencias",
         description="Creando dependencias entre tareas",
         schedule_interval="@once",
         start_date=datetime(2022, 8, 1)) as dag:
    
    t1 = PythonOperator(task_id="tarea1",
                        python_callable=print_mensaje)
    
    t2 = BashOperator(task_id="tarea2",
                      bash_command="echo 'ahora yo soy tarea 2'")
    
    t3 = BashOperator(task_id="tarea3", 
                      bash_command="echo 'me llamo tarea 3'")
    
    t4 = BashOperator(task_id="tarea4", 
                      bash_command="echo 'conmigo termina, soy tarea 4'")
    
    t1.set_downstream([t2,t3])
    t3 >> t4