import random

a = random.randint(10, 101)

print(a)

f = open('/home/roman/airflow/dags/rate.txt', 'w')

f.write(str(a))

f.close()
