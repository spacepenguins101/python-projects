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
current_user = []

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

def display_login_options():
    print("\nAccount Actions")
    print("---------------")
    print("[1] Register")
    print("[2] Login")
    print("[3] Change Password")
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
    cr.execute("INSERT INTO accounts (name, username, password) VALUES (?, ?, ?)", (name, username, password))
    
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
    cr.execute("SELECT * FROM accounts")
    accounts_list = cr.fetchall()
    
    #Commit our connection
    users_conn.commit()

    #Close Connection
    users_conn.close()

    return accounts_list

def update_account(username, new_password):
    #Connect to database
    users_conn = sqlite3.connect('users.db')

    #Create cursor
    cr = users_conn.cursor()
    
    #Update user information
    cr.execute("""
               UPDATE accounts
               SET password = (?)
               WHERE username = (?)
               """, (new_password, username))
    
    cr.execute("SELECT * FROM accounts")
    
    #Get the user account information.
    accounts_list = cr.fetchall()
    
    #Commit our connection
    users_conn.commit()

    #Close Connection
    users_conn.close()

    return accounts_list
#Main Program

#Register / Login functionality
while not login_successful:
    display_login_options()
    acc_option = input("\nAccount option: ")

    if acc_option == "1":
        name, username, password = user_register()
        insert_account(name, username, password)
        accounts = get_accounts()
    elif acc_option == "2":
        while login_attempts != 0 and login_successful == False:
            uname = input("Username: ")
            passwd = input("Password: ")

            accounts = get_accounts()

            for acc in accounts:
                if uname == acc[1] and passwd == acc[2]:
                    print("Login successful!")
                    login_successful = True
                    for i in range(3):
                        current_user.append(acc[i])
                    break
            
            login_attempts -= 1
            if not login_successful and login_attempts != 0:
                print("Wrong credentials. Attempts remaining:", login_attempts)
            elif not login_successful and login_attempts == 0:
                print("Seems like you have trouble logging in. Please create a new account or change your password.")

        login_attempts = 3

    elif acc_option == "3":
        user = input("Enter username: ")
        new_password = input("Enter new password: ")
        new_password2 = input("Re-enter password to confirm: ")

        if new_password == new_password2:  
            acc_list = update_account(user, new_password)
            print(acc_list)
        else:
            print("Different passwords detected. Please try again.")
    
    else:
        confirm_exit = input("Confirm exit (Y or N): ")

        if confirm_exit == "Y": break

if login_successful: 
    print("\nWelcome, " + current_user[0] + "!")
    print()
    display_menu()    