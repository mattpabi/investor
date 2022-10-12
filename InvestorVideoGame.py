import os
import time
from sys import platform

########## DEFINING FUNCTIONS ##########

# CLEAR USER TERMINAL AFTER CHECKING THEIR OPERATING SYSTEM
def clear_terminal():
    if platform == "linux" or platform == "linux2": # LINUX
        os.system("clear")

    elif platform == "darwin": # APPLE / MAC
        os.system("clear")

    elif platform == "win32": # WINDOWS
        os.system("cls")

    else:
        os.system("cls")


# PRINT A NEW LINE
def empty_line():
    print("\n")


# NEW WINDOW: CLEAR TERMINAL + ADD NEW LINE
def start_new_window():
    clear_terminal()
    empty_line()


# DISPLAY THE RULES OF THE GAME
def display_rules():
    print("+-------------------------------------------------------------------------  ABOUT THE GAME  --------------------------------------------------------------------------+")
    print("|                                                                                                                                                                     |")
    print("|    This game is an investing simulation that enables players to learn the risks and rewards involved in the decision-making and risk-taking of financial markets.   |")
    print("|                                                                                                                                                                     |")
    print("|    You will start off with a balance of $100,000 to invest and grow your money through your chosen asset(s).                                                        |")
    print("|    Your goal is to win the challenge by growing your money into $1,000,000.                                                                                         |")
    print("|                                                                                                                                                                     |")
    print("|    A fully randomised set of economic events will be presented to you, and you will be given the option to buy, hold, or sell.                                      |")
    print("|    In order to win the game, you must search for clues in the news, read between the lines, and play some hunches.                                                  |")
    print("|                                                                                                                                                                     |")
    print("|    The game will end once you have beat the challenge, or run out of money.                                                                                         |")
    print("|                                                                                                                                                                     |")
    print("+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+")


# PRESS ANY KEY TO CONTINUE OR TYPE "QUIT" TO QUIT
def continue_or_quit():
    CorQ = input("Press any key to continue, or type 'QUIT' to quit the game.")
    CorQ_lower = CorQ.lower()

    if CorQ_lower == "quit":
        print("Come back next time when you are ready, see you soon.")
        quit()
    
    time.sleep(1)


# DISPLAY INVESTMENT OPTIONS
def display_ivestment_options():
    print("+--------  INVESTMENT OPTIONS  --------+")
    print("|                                      |")
    print("+--  Number  ---  Class  --------------+")
    print("|    1            Stocks               |")
    print("|    2            Real estate          |")
    print("|    3            Lottery tickets      |")
    print("|    4            Cryptocurrencies     |")
    print("|                                      |")
    print("+--------------------------------------+")

    

########## INTRO ##########

clear_terminal()

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


print(ready_for_rules_lower)
time.sleep(1)

if ready_for_rules_lower != "yes":
    print("You are inexperienced and will get rekt.")
    print("Come back next time when you are ready, see you soon.")
    quit()

print("Let's begin")
time.sleep(1)


########## DISPLAY RULES ##########

clear_terminal()

display_rules()

empty_line()
continue_or_quit()

empty_line()
display_ivestment_options()

empty_line()
continue_or_quit()
