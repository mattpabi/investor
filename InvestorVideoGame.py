import os
import time
import random
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


# STOCKS DICTIONARY
stocks_dict = {
    "Apple, Inc. (AAPL)" : round(float(168.49),2),
    "Microsoft Corp. (MSFT)" : round(float(287.02),2),
    "Alphabet, Inc. (GOOGL)" : round(float(118.84),2),
    "Amazon.com, Inc. (AMZ)" : round(float(140.64),2),
    "Tesla, Inc. (TSLA)" : round(float(859.89),2),
    "Berkshire Hathaway (BKR-B)" : round(float(296.47),2),
    "Meta Platforms, Inc. (META)" : round(float(177.49),2),
    "Netflix, Inc. (NFLX)" : round(float(242.70),2)
}


# DISPLAY INVESTMENT OPTIONS
def display_stocks():
    print("+-------------------------  INVESTMENT OPTIONS  ------------------------+")
    print("|                                                                       |")
    print("+--- Ticker ----- Company ---------------------------------- Price -----+")
    print("|    AAPL         Apple, Inc.                                $168.49    |")
    print("|    MSFT         Microsoft Corp.                            $287.02    |")
    print("|    GOOGL        Alphabet, Inc. (Google)                    $118.84    |")
    print("|    AMZ          Amazon.com, Inc.                           $140.64    |")
    print("|    TSLA         Tesla, Inc.                                $859.89    |")
    print("|    BKR-B        Berkshire Hathaway, Inc.                   $296.47    |")
    print("|    META         Meta Platforms, Inc. (FKA Facebook)        $177.49    |")
    print("|    NFLX         Netflix, Inc.                              $242.70    |")
    print("|                                                                       |")
    print("+-----------------------------------------------------------------------+")


# PLAYER INVESTMENT OPTION - ASSIGNING TO ASSET CLASS

def assign_player_investment(investment_choice):

    investment_choice_lower = investment_choice.lower()


    if investment_choice_lower == " ":

        investment_choice = "N/A"
        investment_choice_profile = "N/A"
    

    elif investment_choice_lower == "aapl" or investment_choice_lower == "apple, inc." or investment_choice_lower == "apple":

        investment_choice_profile = "Apple, Inc. engages in the design, manufacture, and sale of smartphones, personal computers, tablets, wearables and accessories, and other varieties of related services."


    elif investment_choice_lower == "msft" or investment_choice_lower == "microsoft corp." or investment_choice_lower == "microsoft":

        investment_choice_profile = "Microsoft Corp. engages in the development and support of software, services, devices, and solutions."


    elif investment_choice_lower == "googl" or investment_choice_lower == "alphabet" or investment_choice_lower == "alphabet, inc." or investment_choice_lower == "google":

        investment_choice_profile = "Alphabet, Inc. is a holding company, which engages in the business of acquisition and operation of different companies, such as its main internet products: ads, Android, Chrome, hardware, Google Cloud, Google Maps, Google Play, Search, and YouTube."

    
    elif investment_choice_lower == "amz" or investment_choice_lower == "amazon.com" or investment_choice_lower == "amazon.com, inc." or investment_choice_lower == "amazon":

        investment_choice_profile = "Amazon.com, Inc. is a multinational technology company, which engages in the provision of online retail shopping services."


    elif investment_choice_lower == "tsla" or investment_choice_lower == "tesla, inc." or investment_choice_lower == "tesla":
        
        investment_choice_profile = "Tesla, Inc. engages in the design, development, manufacture, and sale of fully electric vehicles and energy generation and storage systems."
    

    elif investment_choice_lower == "bkr-b" or investment_choice_lower == "berkshire hathaway, inc." or investment_choice_lower == "berkshire hathaway":

        investment_choice_profile = "Berkshire Hathaway, Inc. engages in the provision of property and casualty insurance and reinsurance, utilities and energy, freight rail transportation, finance, manufacturing, and retailing services."
    

    elif investment_choice_lower == "meta" or investment_choice_lower == "meta platforms, inc." or investment_choice_lower == "meta platforms" or investment_choice_lower == "meta":
        
    
    elif investment_choice_lower == "nflx" or investment_choice_lower == "netflix, inc." or investment_choice_lower == "netflix":
   


    return investment_choice


# DISPLAY PLAYER INVESTMENT ASSET PROFILE
def display_player_investment_asset_profile():
    asset = assign_player_investment()
    
    if asset == "Meta Platforms, Inc. (META)":
        investment_choice_profile = "Meta Platforms, Inc., engages in the development of social media applications. It builds technology that helps people connect, find communities, and grow businesses."

    elif asset == "Netflix, Inc. (NFLX)":
        investment_choice_profile = "Netflix, Inc. operates as a streaming entertainment service company. The firm provides subscription service streaming movies and television episodes over the internet."

    return investment_choice_profile

# DISPLAY PLAYER PORTFOLIO
def display_player_portfolio():
    print(f"______________________________  PORTFOLIO  ______________________________\n")
    print(f"   Open positions                             1                          \n")

    print(f"   Invested asset                                       ")
    print(f"   Assets in holding                                                     \n")
    
    print(f"   ($) Current price")
    print(f"   ($) Current total value")
    print(f"   ($) Price when bought")
    print(f"   ($) Total acquisition cost \n")

    print(f"   ($) Current portfolio value")
    print(f"   ($) Profit / Loss \n")
    print("__________________________________________________________________________")


########## INTRO ##########

# BALANCES
balance_cash = float("100000")
balance_portfolio = float("0")
balance_portfolio_pnl = float("0")


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

display_stocks()


# INPUT INVESTMENT
empty_line()
player_investment = input("Please input the your desired stock to invest in: ")


# RETURN THE STOCK: NAME & TICKER, DESCRIPTION, PRICE from the function
# calls the function to assign the player's choice
assigned_investment, assigned_desc = assign_player_investment(player_investment)

# returns value of dictionary (returns the buying price of player)
assigned_buyPrice = assigned_investment.get(player_investment)
print(assigned_buyPrice) #prints none

# list out keys and values separately
buyPrice_list = list(assigned_investment.values())
buyName_list = list(assigned_investment.keys())

# assigned_name = assigned_investment.values().index(assigned_buyPrice)
assigned_name = buyPrice_list.index(assigned_buyPrice)


# CALCULATIONS FOR THE STOCK PRICE
bought_shares = round(float(balance_cash / assigned_buyPrice),0)

empty_line()

print(f"You have bought {bought_shares} shares of {assigned_name} at ${assigned_buyPrice}.")
print(assigned_desc)

time.sleep(10)

empty_line()

print(f"")
