'''
Project Aim
-----------
This project seeks to help people track their expenses.

Basic Functionality
-------------------
1. Add expenses
2. View specific expenses
3. Edit and delete expenses
4. Calculate statistics
'''
#Modules
import sqlite3

#Variables
login_attempts = 3
login_successful = False

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

def user_register():
    name = input("Enter your first name: ")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    return name, username, password

def insert_account(name, username, password):
    #Connect to database
    users_conn = sqlite3.connect('users.db')

    #Create cursor
    cr = users_conn.cursor()

    #Insert values into table
    cr.execute("INSERT INTO users (name, username, password) VALUES (?, ?, ?, ?)", (name, username, password))
    
    #Commit our connection
    users_conn.commit()

    #Close Connection
    users_conn.close()

def get_accounts():
    #Connect to database
    users_conn = sqlite3.connect('users.db')

    #Create cursor
    cr = users_conn.cursor()
    
    #Get the users.
    cr.execute("SELECT * FROM users")
    accounts_list = cr.fetchall()
    
    #Commit our connection
    users_conn.commit()

    #Close Connection
    users_conn.close()

    return accounts_list

#Main Program
display_menu()


