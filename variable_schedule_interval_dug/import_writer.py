from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from prog import readname, writename
import sys

f = open('/home/roman/airflow/dags/rate.txt', 'r')
a = int(f.readline())
f.close()

file_name1 = '/home/roman/airflow/dags/file1.txt'


default_args = {'owner': 'Airflow', 'start_date': datetime(2018, 8, 22)}


dag = DAG('import_write', default_args=default_args, schedule_interval=timedelta(seconds=a))

progread = PythonOperator(task_id='task1', python_callable=readname, op_kwargs={'file': file_name1}, dag=dag)

progwrite = PythonOperator(task_id='task2', python_callable=writename, provide_context=True, dag=dag)

progread >> progwrite
