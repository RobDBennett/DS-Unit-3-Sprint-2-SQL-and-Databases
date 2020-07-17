#!/usr/bin/env python

import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

create_table_statement = """
CREATE TABLE demo (
    id SERIAL PRIMARY KEY,
    s VARCHAR(1),
    x INTEGER,
    y INTEGER
);
"""

insert_g = """
INSERT INTO demo
(s, x, y)
VALUES ('g', 3, 9);
"""
insert_v= """
INSERT INTO demo
(s, x, y)
VALUES ('v', 5, 7);
"""
insert_f = """
INSERT INTO demo
(s, x, y)
VALUES ('f', 8, 7);
"""
curs.execute(create_table_statement)
curs.execute(insert_g)
curs.execute(insert_v)
curs.execute(insert_f)
conn.commit()

count_rows = 'SELECT COUNT (*) FROM demo;'
print("There are", curs.execute(count_rows).fetchall()[0][0], " rows.")

query2 = 'SELECT COUNT (*) FROM demo WHERE x >= 5 AND y >= 5;'
print("There are", curs.execute(query2).fetchall()[0][0], " rows where and X and Y are at least 5.")

query3 = 'SELECT COUNT(DISTINCT y) FROM demo;'
print("There are", curs.execute(query3).fetchall()[0][0], " unique values of y.")

