#!/usr/bin/env python

"""Assignment notes:
- How many total Characters are there?
- How many of each specific subclass?
- How many total Items?
- How many of the Items are weapons? How many are not?
- How many Items does each character have? (Return first 20 rows)
- How many Weapons does each character have? (Return first 20 rows)
- On average, how many Items does each Character have?
- On average, how many Weapons does each character have?
"""

import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

count_characters = 'SELECT COUNT (*) FROM charactercreator_character;'
print("Total character count is:", curs.execute(count_characters).fetchall()[0][0])

count_mages = 'SELECT COUNT (*) FROM charactercreator_mage;'
count_fighter = 'SELECT COUNT (*) FROM charactercreator_fighter;'
count_necro = 'SELECT COUNT (*) FROM charactercreator_necromancer;'
count_thief = 'SELECT COUNT (*) FROM charactercreator_thief;'
count_cleric = 'SELECT COUNT (*) FROM charactercreator_cleric;'
print("Total Mages:", curs.execute(count_mages).fetchall()[0][0])
print("Total Fighter:", curs.execute(count_fighter).fetchall()[0][0])
print("Total Necromancers:", curs.execute(count_necro).fetchall()[0][0])
print("Total Thieves:", curs.execute(count_thief).fetchall()[0][0])
print("Total Clerics:", curs.execute(count_cleric).fetchall()[0][0])

total_items = 'SELECT COUNT (*) FROM armory_item;'
print("Total number of Items:", curs.execute(total_items).fetchall()[0][0])

weapons = 'SELECT COUNT (*) FROM armory_item, armory_weapon WHERE armory_item.item_id = armory_weapon.item_ptr_id;'
print("Total Weapons:", curs.execute(weapons).fetchall()[0][0])

print("Total Non-Weapon Items:", curs.execute(total_items).fetchall()[0][0] - curs.execute(weapons).fetchall()[0][0])

char_items = (f'SELECT COUNT (*) FROM charactercreator_character JOIN charactercreator_character_inventory ON ' 
            f'charactercreator_character.character_id = charactercreator_character_inventory.character_id GROUP BY' 
            f' charactercreator_character_inventory.character_id')

x = range(0, 20)

char_weapons = (f'SELECT COUNT (*) FROM charactercreator_character JOIN charactercreator_character_inventory ON ' 
            f'charactercreator_character.character_id = charactercreator_character_inventory.character_id JOIN armory_weapon'
            f' ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id '
            f'GROUP BY charactercreator_character_inventory.character_id')

for _ in x:
    print("Character", _ + 1, "has ", curs.execute(char_items).fetchall()[_][0], "items and", 
    curs.execute(char_weapons).fetchall()[_][0], "weapons.")

#Alternate query for averages:

"""
SELECT AVG(num_items) FROM
(SELECT cc.character_id, COUNT(DISTINCT ai.item_id) AS num_items
FROM charactercreator_character AS cc,
charactercreator_character_inventory AS cci,
armory_item AS ai
WHERE cc.character_id = cci.character_id
AND ai.item_id = cci.item_id
GROUP BY 1);
"""

y = range(0,302)
test = range(0,155)
item_count = 0
weapon_count = 0
for _ in y:
    item_count = item_count + curs.execute(char_items).fetchall()[_][0]

print("The average items per character is: ", item_count / 302)

for _ in test:
    weapon_count = weapon_count + curs.execute(char_weapons).fetchall()[_][0]

print("The average weapons per character is: ", weapon_count / 155)