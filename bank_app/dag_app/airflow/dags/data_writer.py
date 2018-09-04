import psycopg2
from psycopg2 import sql

def create_table(table):
    conn = psycopg2.connect("host=database dbname=currency user=postgres password=postgres")
    cur = conn.cursor()
    command = sql.SQL("CREATE TABLE {} (id serial PRIMARY KEY, time date, ccy VARCHAR(3), base_ccy VARCHAR(3), buy float, sale float, bank VARCHAR(255));").format(sql.Identifier(table))
    cur.execute(command)
    conn.commit()

def create_nbu_table(table):
    conn = psycopg2.connect("host=database dbname=currency user=postgres password=postgres")
    cur = conn.cursor()
    command = sql.SQL("CREATE TABLE {} (id serial PRIMARY KEY, Дата date, Код_цифровий VARCHAR(3), Код_літерний VARCHAR(3), Кількість_одиниць float, Назва_валюти VARCHAR(255), Офіційний_курс float);").format(sql.Identifier(table))
    cur.execute(command)
    conn.commit()

def insert(table, a):
    conn = psycopg2.connect("host=database dbname=currency user=postgres password=postgres")
    cur = conn.cursor()
    command = sql.SQL("INSERT INTO {} (time, ccy, base_ccy, buy, sale, bank) VALUES (%s, %s, %s, %s, %s, %s);").format(sql.Identifier(table))
    cur.execute(command, a)
    conn.commit()

def insert_nbu(table, a):
    conn = psycopg2.connect("host=database dbname=currency user=postgres password=postgres")
    cur = conn.cursor()
    command = sql.SQL("INSERT INTO {} (Дата, Код_цифровий, Код_літерний, Кількість_одиниць, Назва_валюти, Офіційний_курс) VALUES (%s, %s, %s, %s, %s, %s);").format(sql.Identifier(table))
    cur.execute(command, a)
    conn.commit()

def select(table):
    conn = psycopg2.connect("host=database dbname=currency user=postgres password=postgres")
    cur = conn.cursor()
    command = sql.SQL("SELECT time FROM {} ORDER BY id DESC LIMIT 1;").format(sql.Identifier(table))
    cur.execute(command)
    records = cur.fetchall()
    return records

def select_nbu(table):
    conn = psycopg2.connect("host=database dbname=currency user=postgres password=postgres")
    cur = conn.cursor()
    command = sql.SQL("SELECT Дата FROM {} ORDER BY id DESC LIMIT 1;").format(sql.Identifier(table))
    cur.execute(command)
    records = cur.fetchall()
    return records

'''def multiinsert(table, time, currency, base, buy, sale, bank):
    conn = psycopg2.connect("host=localhost dbname=currency user=postgres password=postgres")
    cur = conn.cursor()
    args = [time, (currency1]
    command = sql.SQL("INSERT INTO {} (time, ccy, base_ccy, buy, sale, bank) VALUES (%s, %s, %s, %s, %s, %s);").format(sql.Identifier(table))

def update(currency, buy, sell):
    conn = psycopg2.connect("host=localhost dbname=currency user=postgres password=postgres")
    cur = conn.cursor()
    cur.execute(
        "UPDATE exchange SET buy=(%s), sell=(%s) WHERE ccy=(%s);",
        (buy, sell, currency)
    )
    conn.commit()

#        "INSERT INTO exchange VALUES (%s, %s, %s);",
#        (currency, buy, sell)'''

