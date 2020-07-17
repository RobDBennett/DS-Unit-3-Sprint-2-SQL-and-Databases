#!/usr/bin/env python

import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

query1 = """
SELECT MAX(UnitPrice), ProductName FROM Product 
GROUP BY UnitPrice ORDER BY UnitPrice DESC LIMIT 10;"""
print("The ten most expensive items are", curs.execute(query1).fetchall())

query2 = "SELECT AVG(age) FROM (SELECT HireDate - Birthdate AS age FROM Employee);"
print("The average age of new employees is:",
      curs.execute(query2).fetchall()[0][0])

query3 = """
SELECT MAX(UnitPrice), ProductName, CompanyName FROM Product, Supplier 
WHERE Product.SupplierID = Supplier.Id GROUP BY UnitPrice ORDER BY UnitPrice DESC LIMIT 10;"""
print("The ten most expensive items with product name and suppliers are: ",
      curs.execute(query3).fetchall())

query4 = """
SELECT COUNT (DISTINCT CategoryID), CategoryName FROM Product, 
Category WHERE Category.ID = Product.CategoryId"""
print("The category with the most items in it is:",
      curs.execute(query4).fetchall())

stretch1a = """
SELECT AVG(age) FROM (SELECT HireDate - Birthdate AS age 
FROM Employee WHERE City = 'Seattle');"""
stretch1b = """
SELECT AVG(age) FROM (SELECT HireDate - Birthdate AS age 
FROM Employee WHERE City = 'Kirkland');"""
stretch1c = """
SELECT AVG(age) FROM (SELECT HireDate - Birthdate AS age 
FROM Employee WHERE City = 'London');"""
stretch1d = """
SELECT AVG(age) FROM (SELECT HireDate - Birthdate AS age 
FROM Employee WHERE City = 'Tacoma');"""
stretch1e = """
SELECT AVG(age) FROM (SELECT HireDate - Birthdate AS age 
FROM Employee WHERE City = 'Redmond');"""
print("The average age for new hires in Seattle is ",
      curs.execute(stretch1a).fetchall()[0][0])
print("The average age for new hires in Kirkland is ",
      curs.execute(stretch1b).fetchall()[0][0])
print("The average age for new hires in London is ",
      curs.execute(stretch1c).fetchall()[0][0])
print("The average age for new hires in Tacoma is ",
      curs.execute(stretch1d).fetchall()[0][0])
print("The average age for new hires in Redmond is ",
      curs.execute(stretch1e).fetchall()[0][0])

stretch2 = """
SELECT COUNT(DISTINCT TerritoryID) AS Counts, EmployeeID, FirstName 
FROM EmployeeTerritory, Employee WHERE EmployeeTerritory.EmployeeId = Employee.Id 
GROUP BY EmployeeId ORDER BY Counts DESC LIMIT 1;"""
print("The Employee with the most Territories is: ", curs.execute(stretch2).fetchall()[
      0][2], " with ", curs.execute(stretch2).fetchall()[0][0], " territories.")
