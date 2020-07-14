#!/usr/bin/env python

"""Assignment notes:
1- Use Pandas to import the buddy csv. Should be 249 rows, 7 columns, no nulls.
2- Use sqlite3, open a connection to a new database 'buddymove_holidayiq.sqlite3'
3- Use df.to_sql.  Might need the 'review' command.
4- Using sql queries- 
* Count how many rows you have (should be 249)
* How many users who reviewed at least 100 'Nature' also reviewed at least '100' in Shopping.
* (stretch) What are the average number of reviews for each category?
"""

import pandas as pd
import sqlite3

df = pd.read_csv('buddymove_holidayiq.csv')
print(df.shape)

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = conn.cursor()
df.to_sql('review', conn)

counts = 'SELECT COUNT (*) FROM review;'

print("Total number of users:", curs.execute(counts).fetchall()[0][0])

assign2 = 'SELECT COUNT (*) FROM review WHERE Nature >= 100 AND Shopping >= 100'

print("Users who had at least 100 in both nature and shopping", curs.execute(assign2).fetchall()[0][0])