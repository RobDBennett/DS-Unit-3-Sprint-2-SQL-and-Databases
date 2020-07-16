#!/usr/bin/env python

"""
Assignment Notes:
Answer questions for RPG using mongo DP
- How many total Characters are there?
- How many of each specific subclass?
- How many total Items?
- How many of the Items are weapons? How many are not?
- How many Items does each character have? (Return first 20 rows)
- How many Weapons does each character have? (Return first 20 rows)
- On average, how many Items does each Character have?
- On average, how many Weapons does each character have?
** The above has been listed as stretch goals in class **
Answer these questions with the PostGre
- How many passengers survived, and how many died?
- How many passengers were in each class?
- How many passengers survived/died within each class?
- What was the average age of survivors vs nonsurvivors?
- What was the average age of each passenger class?
- What was the average fare by passenger class? By survival?
- How many siblings/spouses aboard on average, by passenger class? By survival?
- How many parents/children aboard on average, by passenger class? By survival?
- Do any passengers have the same name?
- (Bonus! Hard, may require pulling and processing with Python) How many married
  couples were aboard the Titanic? Assume that two people (one `Mr.` and one
  `Mrs.`) with the same last name and with at least 1 sibling/spouse aboard are
  a married couple.
"""

import pandas as pd
import psycopg2
import sqlite3
#import pymongo

dbname = 'lzczcioo'
user = 'lzczcioo'
password = 'SKXlgDub9VjsNCooGYnndDogc-AgP_F_'
host = 'ruby.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)

# client = pymongo.MongoClient(
#    "mongodb+srv://RobDBennett:6f6xJlAeZAswx7cV@cluster0.cuiyy.mongodb.net/test?retryWrites=true&w=majority")
#db = client.test

pg_curs = pg_conn.cursor()
pg_curs.execute('SELECT COUNT (*) FROM titanic1 WHERE survived = 0;')
pg_died = pg_curs.fetchall()[0][0]
print(pg_died, " passangers died.")
pg_curs.execute('SELECT COUNT (*) FROM titanic1 WHERE survived = 1;')
pg_survived = pg_curs.fetchall()[0][0]
print(pg_survived, " passangers survived.")
pg_curs.execute('SELECT COUNT (*) FROM titanic1 WHERE pclass = 1;')
pg_pclass1 = pg_curs.fetchall()[0][0]
pg_curs.execute('SELECT COUNT (*) FROM titanic1 WHERE pclass = 2;')
pg_class2 = pg_curs.fetchall()[0][0]
pg_curs.execute('SELECT COUNT (*) FROM titanic1 WHERE pclass = 3;')
pg_class3 = pg_curs.fetchall()[0][0]
print("There were", pg_pclass1, "class 1 passengers,", pg_class2,
      "class 2 passengers and,", pg_class3, " class 3 passengers.")

for _ in range(1,4):
  lived = """SELECT COUNT (*) FROM titanic1 WHERE pclass =""" + str(_) + """ AND survived = 1"""
  pg_curs.execute(lived)
  pg_class_suv = pg_curs.fetchall()[0][0]
  print(pg_class_suv, " passengers survived from class", _)
  died = """SELECT COUNT (*) FROM titanic1 WHERE pclass =""" + str(_) + """ AND survived = 0"""
  pg_curs.execute(died)
  pg_class_dead = pg_curs.fetchall()[0][0]
  print(pg_class_dead, " passengers died from class", _)

pg_curs.execute("SELECT AVG(age) FROM titanic1 WHERE survived=1;")
pg_avg_age_surv = pg_curs.fetchall()[0][0]
print("The average age of a survivor is: ", pg_avg_age_surv)
pg_curs.execute("SELECT AVG(age) FROM titanic1 WHERE survived=0")
pg_avg_age_dead = pg_curs.fetchall()[0][0]
print("The average age of the dead is: ", pg_avg_age_dead)

for _ in range(1,4):
  avg_age = """SELECT AVG(age) FROM titanic1 WHERE pclass=""" + str(_) +""";"""
  pg_curs.execute(avg_age)
  pg_class_age = pg_curs.fetchall()[0][0]
  print("The average age of class ", _, " is ", pg_class_age)

for _ in range(1,4):
  avg_fare = """SELECT AVG(fare) FROM titanic1 WHERE pclass=""" + str(_) +""";"""
  pg_curs.execute(avg_fare)
  pg_class_fare = pg_curs.fetchall()[0][0]
  print("The average fare for class ", _, " is ", pg_class_fare)

pg_curs.execute("SELECT AVG(fare) FROM titanic1 WHERE survived=1;")
pg_fare_surv = pg_curs.fetchall()[0][0]
print("The average fare of a survivor is ", pg_fare_surv)

for _ in range(1,4):
  avg_sib = """SELECT AVG(sibling_spouse_aboard) FROM titanic1 WHERE pclass=""" + str(_) +""";"""
  pg_curs.execute(avg_sib)
  pg_sibs_avg = pg_curs.fetchall()[0][0]
  print("The average number of siblings aboard for class ", _, " is ", pg_sibs_avg)

pg_curs.execute("SELECT AVG(sibling_spouse_aboard) FROM titanic1 WHERE survived=1;")
avg_sib_sur = pg_curs.fetchall()[0][0]
print("The average number of siblings aboard for survivors was ", avg_sib_sur)

for _ in range(1,4):
  avg_child = """SELECT AVG(parents_children_aboard) FROM titanic1 WHERE pclass=""" + str(_) +""";"""
  pg_curs.execute(avg_child)
  pg_avg_child = pg_curs.fetchall()[0][0]
  print("The average number of children/parents aboard for class ", _, " is ", pg_avg_child)

pg_curs.execute("SELECT AVG(parents_children_aboard) FROM titanic1 WHERE survived=1;")
avg_child_sur = pg_curs.fetchall()[0][0]
print("The average number of children/parents aboard for survivors was", avg_child_sur)

pg_curs.execute("SELECT COUNT (name) FROM titanic1 GROUP BY name HAVING ( COUNT(name) > 1 );")
dup_names = pg_curs.fetchall()
print("There were ", dup_names, " passengers with the same names.")
