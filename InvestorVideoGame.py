import os
import time
from sys import platform

########## DEFINING FUNCTIONS ##########

##### Check user's operating system and clears the terminal
def clear_terminal():
    if platform == "linux" or platform == "linux2": # LINUX
        os.system("clear")

    elif platform == "darwin": # APPLE / MAC
        os.system("clear")

    elif platform == "win32": # WINDOWS
        os.system("cls")

clear_terminal()


##### Prints a new line, to have all printed text one line under the top of the terminal window
def empty_line():
    print("\n")


#####
def start_new_window():
    clear_terminal()
    empty_line()


########## INTRO ##########

clear_terminal()
empty_line()

username = input("Hello there! Please enter your desired username: ")

print(f"""
Hello, {username}, and welcome to:

/$$                                           /$$
|__/                                          | $$
/$$ /$$$$$$$  /$$    /$$ /$$$$$$   /$$$$$$$ /$$$$$$    /$$$$$$   /$$$$$$
| $$| $$__  $$|  $$  /$$//$$__  $$ /$$_____/|_  $$_/   /$$__  $$ /$$__  $$
| $$| $$  \ $$ \  $$/$$/| $$$$$$$$|  $$$$$$   | $$    | $$  \ $$| $$  \__/
| $$| $$  | $$  \  $$$/ | $$_____/ \____  $$  | $$ /$$| $$  | $$| $$
| $$| $$  | $$   \  $/  |  $$$$$$$ /$$$$$$$/  |  $$$$/|  $$$$$$/| $$
|__/|__/  |__/    \_/    \_______/|_______/    \___/   \______/ |__/

""")

ready_for_rules = input("Are you ready to review the rules? (yes/no): ")

ready_for_rules_lower = ready_for_rules.lower()

if ready_for_rules_lower == "yes":
    print("Let's begin")

else:
    print("You are inexperienced and will get rekt.")
    print("Come back next time when you are ready, see you soon.")
    quit()


##### Dislay rules

clear_terminal()

print("The goal of this game is to make money.")
