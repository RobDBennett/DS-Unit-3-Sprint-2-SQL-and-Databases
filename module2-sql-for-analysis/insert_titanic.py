#!/usr/bin/env python

"""Assignment notes:
Then, set up a new table for the Titanic data (`titanic.csv`) - spend some time
thinking about the schema to make sure it is appropriate for the columns.
[Enumerated types](https://www.postgresql.org/docs/9.1/datatype-enum.html) may
be useful. Once it is set up, write a `insert_titanic.py` script that uses
`psycopg2` to connect to and upload the data from the csv, and add the file to
your repo. Then start writing PostgreSQL queries to explore the data!
"""
import pandas as pd
import psycopg2
import sqlite3

df = pd.read_csv('titanic.csv')
df['Name'] = df['Name'].str.replace("'", " ")
print(df.shape)

conn = sqlite3.connect('titanic.sqlite3')
curs = conn.cursor()
df.to_sql('titanic', conn)

sl_conn = sqlite3.connect('titanic.sqlite3')
sl_curs = sl_conn.cursor()

get_titanic = 'SELECT * FROM titanic;'
passangers = sl_curs.execute(get_titanic).fetchall()

dbname = 'lzczcioo'
user = 'lzczcioo'  # ElephantSQL chooses to reuse dbname and username
password = 'SKXlgDub9VjsNCooGYnndDogc-AgP_F_'
host = 'ruby.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)

create_table_statement = """
CREATE TABLE titanic1 (
    id SERIAL PRIMARY KEY,
    survived INTEGER,
    pclass INTEGER,
    name VARCHAR(120),
    sex VARCHAR(10),
    age FLOAT(1),
    sibling_spouse_aboard INTEGER,
    parents_children_aboard INTEGER,
    fare FLOAT(4)
);
"""
pg_curs = pg_conn.cursor()
pg_curs.execute(create_table_statement)


for passanger in passangers:
    insert_passanger = """
    INSERT INTO titanic1
    (survived, pclass, name, sex, age, 
    sibling_spouse_aboard, parents_children_aboard, fare)
    VALUES""" + str(passanger[1:]) + ";"
    pg_curs.execute(insert_passanger)

pg_conn.commit()