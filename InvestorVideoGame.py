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
    print("+--- Number ----- Class ---------------+")
    print("|    1            Stocks               |")
    print("|    2            Real estate          |")
    print("|    3            Lottery tickets      |")
    print("|    4            Cryptocurrencies     |")
    print("|                                      |")
    print("+--------------------------------------+")


# PLAYER INVESTMENT OPTION - INITIALISE FOR PORTFOLIO
player_assetClass = " "
player_assetClass_lower = player_assetClass.lower()

# PLAYER INVESTMENT OPTION - ASSIGNING TO ASSET CLASS
def assign_player_assetClass():
    if player_assetClass == "1":
        player_assetClass == "Stocks"

    elif player_assetClass_lower == "stocks" or "equities" or "stock market":
        player_assetClass == "Stocks"

    elif player_assetClass == "2":
        player_assetClass == "Real estate"
    
    elif player_assetClass_lower == "real estate":
        player_assetClass == "Real estate"

    elif player_assetClass == "3":
        player_assetClass == "Lottery tickets"
    
    elif player_assetClass_lower == "lottery tickets" or "lottery":
        player_assetClass == "Lottery tickets"
    
    elif player_assetClass == "4":
        player_assetClass == "Cryptocurrencies"
    
    elif player_assetClass_lower == "cryptocurrencies" or "crypto":
        player_assetClass == "Cryptocurrencies"


# DISPLAY PLAYER PORTFOLIO
def display_player_portfolio():
    print(f"______________________________  PORTFOLIO  ______________________________\n")
    print(f"   Open positions                             1 \n")

    print(f"   Invested asset class                       {player_assetClass}")
    print(f"   INvested asset                   ")
    print(f"   Assets in holding \n")
    
    print(f"   ($) Current price")
    print(f"   ($) Current total value")
    print(f"   ($) Price when bought")
    print(f"   ($) Total acquisition cost \n")

    print(f"   ($) Current portfolio value")
    print(f"   ($) Profit / Loss \n")
    print("__________________________________________________________________________")


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

time.sleep(0.5)

if ready_for_rules_lower != "yes":
    empty_line()
    print("You are inexperienced and will get rekt.")
    print("Come back next time when you are ready, see you soon.")
    empty_line()
    quit()

print("> Let's begin")

print("\nFor the best experience, please make sure that you are playing this game in fullscreen.")

empty_line()
continue_or_quit()

########## DISPLAY RULES ##########

clear_terminal()

display_rules()

empty_line()
continue_or_quit()

########## DISPLLAY INVESTMENT OPTIONS ##########

clear_terminal()

display_ivestment_options()

empty_line()
player_assetClass = input("Please input the your desired asset class to invest in: ")
print(f"> You have chosen to invest in {player_assetClass}.")
print("Here are the available assets in this class:")

empty_line()

display_player_portfolio()
