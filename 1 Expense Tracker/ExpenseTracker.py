'''
Project Aim
-----------
This project seeks to help people track their expenses better and faster.

Basic Functionality
-------------------
1. Add expenses
2. View specific expenses
3. Edit and delete expenses
4. Calculate statistics
'''
#Modules
import sqlite3

#Functions
def display_menu():
    print("Options")
    print("-------")
    print("[1] Add new expense")
    print("[2] View all expenses")
    print("[3] Edit expense")
    print("[4] Delete expense(s)")
    print("[5] View statistics of expenses")
    print("[0] Exit")

#Database Intialisation

#Connect to database
conn = sqlite3.connect('users.db')

#Create cursor
cr = conn.cursor()

#Create a table
cr.execute("""
    CREATE TABLE users (
           first_name text,
           last_name text,
           username text,
           password text
    )
""")

#Commit our connection
conn.commit()

#Close Connection
conn.close()

#Main Program
display_menu()