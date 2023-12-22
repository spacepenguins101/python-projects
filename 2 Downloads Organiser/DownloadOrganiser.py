# Modules
from pathlib import Path

# Variables
user_input = None
DOWNLOAD = Path.home() / 'Downloads'

# Functions
def display_menu():
    print("\nMenu Options")
    print("------------")
    print("[1] Organise download files")
    print("[2] Remove old files")
    print("[0] Exit")

# Main Program
while user_input != "0":
    display_menu()
    user_input = input("\nEnter you option: ")

    match user_input:
        case "1":
            print(DOWNLOAD)
        case "2":
            print("You chose option 2.")
        case "0":
            break
        case _:
            print("Invalid option! Please enter your option again!")