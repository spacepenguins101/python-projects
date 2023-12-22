# Variables
user_input = None

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