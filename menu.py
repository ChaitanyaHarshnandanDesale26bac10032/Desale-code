# menu.py
"""
Menu file for Cricket Team Selector
Beginner-friendly and simple to understand
"""

def show_main_menu():
    print("\n" + "******************************************")
    print("CRICKET TEAM SELECTOR MENU")
    print("******************************************")
    print("1. Add players")
    print("2. Select playing 11")
    print("3. Show selected team")
    print("4. Exit")
    print("******************************************")


def get_choice():
    while True:
        choice = input("Enter your choice (1-4): ")

        if choice.isdigit():
            choice = int(choice)

            if choice >= 1 and choice <= 4:
                return choice

        print("Oops! Please enter a valid number from 1 to 4.")


def show_sub_menu():
    print("\n" + "*" * 50)
    print("TEAM VIEW OPTIONS")
    print("*" * 50)
    print("1. Show OPENERS")
    print("2. Show MIDDLE ORDER")
    print("3. Show FINISHERS")
    print("4. Show BOWLING ATTACK / TAIL")
    print("5. Show FULL TEAM")
    print("6. Back to main menu")
    print("*" * 50)


def get_sub_choice():
    while True:
        choice = input("Enter your choice (1-6): ")

        if choice.isdigit():
            choice = int(choice)

            if choice >= 1 and choice <= 6:
                return choice

        print("Oops! Please enter a valid number from 1 to 6.")


def show_exit_message():
    print("\n" + "******************************************")
    print("Thank you for using Cricket Team Selector!")
    print("******************************************")
