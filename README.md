# Apache---Airflow

Este ejercicio se ha realizado bajo el ambiente en Windows usando WSL y Docker Desktop.

Siguiendo los pasos de instalación en la [documentación](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html)

luego pasando estos comandos: 

Traer el documento del docker-compose.yaml, donde están todas las instrucciones de su despliegue. Correr ese comando posicionado en la carpeta de su proyecto. 

````shell
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.9.1/docker-compose.yaml'
````
Luego corresponde crear los directorios con los que funciona normalmente airflow. 

````shell
mkdir -p ./dags ./logs ./plugins
````
````shell
docker compose up airflow-init
````
````shell
docker compose up -d
````
Conectarse al localhost:8080
por defecto, usuario y contraseña, son "airflow". 

Ya puede empezar a crear sus dags, para correrlos. 