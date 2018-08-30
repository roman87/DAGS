from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from time import sleep

stop = '/usr/local/bin/airflow pause import_write'
change = 'python3 ~/airflow/dags/changer.py'
ins = 'python3 ~/airflow/dags/import_writer.py'
run = '/usr/local/bin/airflow unpause import_write'

default_args = {'owner': 'Airflow', 'start_date': datetime(2018, 8, 22)}


dag = DAG('maneger', default_args=default_args, schedule_interval=timedelta(minutes=2), catchup=False)

t1 = BashOperator(task_id='task1', bash_command=stop, dag=dag)

t2 = BashOperator(task_id='task2', bash_command=change, dag=dag)

t3 = BashOperator(task_id='task3', bash_command=ins, dag=dag)

t4 = BashOperator(task_id='task4', bash_command=run, dag=dag)

t1 >> t2 >> t3 >> t4
