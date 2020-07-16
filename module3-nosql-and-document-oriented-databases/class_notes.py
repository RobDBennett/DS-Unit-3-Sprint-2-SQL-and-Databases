#!/usr/bin/env python

"""Assignment notes=
Put the RPG data into Mongo!

Assignment Question= 
"How was working with MongoDB different from working with
PostgreSQL? What was easier, and what was harder?"

Answer= 
I don't think it was any easier or harder; it balanced out.
For instance, I think it's easier to make a mistake in mongo.
The lack of error messages feels real dangerous to me. And the fact
that you can save anything to it without issue is both a benefit and
a bane, since there aren't checks/balances to it.
Not having to build a table first is nice, except that I like the 
structure of a table, so not having it there is actually a bit disorienting.
I'd call it a wash- its just different.
"""
import pandas as pd
import pymongo
import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

get_rpg = 'SELECT * FROM charactercreator_character;'
characters = curs.execute(get_rpg).fetchall()

client = pymongo.MongoClient("mongodb+srv://RobDBennett:6f6xJlAeZAswx7cV@cluster0.cuiyy.mongodb.net/test?retryWrites=true&w=majority")
db = client.test



for char in characters:
    rpg_char = {
        'character_id': char[0],
        'name': char[1],
        'level': char[2],
        'exp': char[3],
        'hp': char[4],
        'strength': char[5],
        'intelligence': char[6],
        'dexterity': char[7],
        'wisdom': char[8]
    }
    db.test.insert_one(rpg_char)

print(db.test.find_one({'name': 'Ali'}))
