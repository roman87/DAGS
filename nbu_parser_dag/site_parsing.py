from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from data_writer import insert_nbu, select_nbu
from pars import Extract



def create_date():
    table = 'nbu'
    d = select_nbu(table)
    if d==[]:
       start = datetime(2018, 1, 1)
       day = str(start.day)
       month = str(start.month)
       year = str(start.year)
       date = day + '.' + month + '.' + year
    else:
       s = str(d[0][0])
       #dt = datetime(int(s[2]), int(s[1]), int(s[0])) + timedelta(days=1)
       dt = datetime.strptime(s, "%Y-%m-%d") + timedelta(days=1)
       day = str(dt.day)
       month = str(dt.month)
       year = str(dt.year)
       date = day + '.' + month + '.' + year       
    return date


def exchange(**kwargs):
    ti = kwargs['ti']
    date = ti.xcom_pull(task_ids='task1')
    s = date.split('.')
    data = datetime(int(s[2]), int(s[1]), int(s[0]))
    year = int(data.year)
    month = int(data.month)
    day = int(data.day)
    da = str(day) + '-' + str(month) + '-' + str(year)
    d = Extract(year, month, day)
    driver = d.open_web()
    matrix = d.get_data()
    d.close_web()
    table = 'nbu'
    a1 = matrix[7]
    a1.insert(0, da)
    a2 = matrix[8]
    a2.insert(0, da)
    a3 = matrix[11]
    a3.insert(0, da)
    insert_nbu(table, a1)
    insert_nbu(table, a2)
    insert_nbu(table, a3)


default_args = {'owner': 'Airflow', 'start_date': datetime(2018, 1, 1)}


dag = DAG('site_parsing', default_args=default_args, schedule_interval=timedelta(days=1), max_active_runs=1)


ex1 = PythonOperator(task_id='task1', python_callable=create_date, dag=dag)

ex2 = PythonOperator(task_id='task2', python_callable=exchange, provide_context=True, dag=dag)

ex1 >> ex2
