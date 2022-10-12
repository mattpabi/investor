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
    print("|    The game will end once you have beat the challenge, or run out of money. You may type QUIT at any time to leave the game.                                        |")
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


# STOCK KEYWORDS (CHECK IF INPUT IS IN THIS LIST)
stocks_keywords_list = ["aapl", "apple, inc.", "apple", "msft", "microsoft corp.", "microsoft", "googl", "alphabet", "alphabet, inc.", "google", "amz", "amazon.com", "amazon.com, inc.", "amazon", "tsla", "tesla, inc.", "tesla", "bkr-b", "berkshire hathaway, inc.", "berkshire hathaway", "meta", "meta platforms, inc.", "meta platforms", "meta", "nflx", "netflix, inc.", "netflix"]


# STOCK CHOICE INPUT CONVERTER
def player_investment_choice_converter(investment_choice):

    investment_choice_lower = investment_choice.lower() 

    if investment_choice_lower == "aapl" or investment_choice_lower == "apple, inc." or investment_choice_lower == "apple":
        investment_choice = "Apple, Inc. (AAPL)"
        return investment_choice
    
    elif investment_choice_lower == "msft" or investment_choice_lower == "microsoft corp." or investment_choice_lower == "microsoft":
        investment_choice = "Microsoft Corp. (MSFT)"
        return investment_choice
    
    elif investment_choice_lower == "googl" or investment_choice_lower == "alphabet" or investment_choice_lower == "alphabet, inc." or investment_choice_lower == "google":
        investment_choice = "Alphabet, Inc. (GOOGL)"
        return investment_choice
    
    elif investment_choice_lower == "amz" or investment_choice_lower == "amazon.com" or investment_choice_lower == "amazon.com, inc." or investment_choice_lower == "amazon":
        investment_choice = "Amazon.com, Inc. (AMZ)"
        return investment_choice

    elif investment_choice_lower == "tsla" or investment_choice_lower == "tesla, inc." or investment_choice_lower == "tesla":
        investment_choice_profile = "Tesla, Inc. (TSLA)"
        return investment_choice

    elif investment_choice_lower == "bkr-b" or investment_choice_lower == "berkshire hathaway, inc." or investment_choice_lower == "berkshire hathaway":
        investment_choice_profile = "Berkshire Hathaway (BKR-B)"
        return investment_choice

    elif investment_choice_lower == "meta" or investment_choice_lower == "meta platforms, inc." or investment_choice_lower == "meta platforms" or investment_choice_lower == "meta":
        investment_choice_profile = "Meta Platforms, Inc. (META)"
        return investment_choice

    elif investment_choice_lower == "nflx" or investment_choice_lower == "netflix, inc." or investment_choice_lower == "netflix":
        investment_choice_profile = "Netflix, Inc. (NFLX)"
        return investment_choice


# PLAYER INVESTMENT OPTION - ASSIGNING TO ASSET CLASS
def assign_player_investment_profile(investment_choice):

    investment_choice_lower = investment_choice.lower() 
    
    if investment_choice_lower == "aapl" or investment_choice_lower == "apple, inc." or investment_choice_lower == "apple":
        investment_choice_profile = "Apple, Inc. engages in the design, manufacture, and sale of smartphones, personal computers, tablets, wearables and accessories, and other varieties of related services."
        return investment_choice_profile

    elif investment_choice_lower == "msft" or investment_choice_lower == "microsoft corp." or investment_choice_lower == "microsoft":
        investment_choice_profile = "Microsoft Corp. engages in the development and support of software, services, devices, and solutions."
        return investment_choice_profile

    elif investment_choice_lower == "googl" or investment_choice_lower == "alphabet" or investment_choice_lower == "alphabet, inc." or investment_choice_lower == "google":
        investment_choice_profile = "Alphabet, Inc. is a holding company, which engages in the business of acquisition and operation of different companies, such as its main internet products: ads, Android, Chrome, hardware, Google Cloud, Google Maps, Google Play, Search, and YouTube."
        return investment_choice_profile
    
    elif investment_choice_lower == "amz" or investment_choice_lower == "amazon.com" or investment_choice_lower == "amazon.com, inc." or investment_choice_lower == "amazon":
        investment_choice_profile = "Amazon.com, Inc. is a multinational technology company, which engages in the provision of online retail shopping services."
        return investment_choice_profile

    elif investment_choice_lower == "tsla" or investment_choice_lower == "tesla, inc." or investment_choice_lower == "tesla":
        investment_choice_profile = "Tesla, Inc. engages in the design, development, manufacture, and sale of fully electric vehicles and energy generation and storage systems."
        return investment_choice_profile

    elif investment_choice_lower == "bkr-b" or investment_choice_lower == "berkshire hathaway, inc." or investment_choice_lower == "berkshire hathaway":
        investment_choice_profile = "Berkshire Hathaway, Inc. engages in the provision of property and casualty insurance and reinsurance, utilities and energy, freight rail transportation, finance, manufacturing, and retailing services."
        return investment_choice_profile

    elif investment_choice_lower == "meta" or investment_choice_lower == "meta platforms, inc." or investment_choice_lower == "meta platforms" or investment_choice_lower == "meta":
        investment_choice_profile = "Meta Platforms, Inc., engages in the development of social media applications. It builds technology that helps people connect, find communities, and grow businesses."
        return investment_choice_profile

    elif investment_choice_lower == "nflx" or investment_choice_lower == "netflix, inc." or investment_choice_lower == "netflix":
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
print("This game was coded in Python 3.10, running this game in prior Python versions may result in glitches or bugs that disrupt the gaming experience.")

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

if player_investment.lower() in stocks_keywords_list:

    player_investment_converted = player_investment_choice_converter(player_investment) # turns player input into code readble string (e.g. "aapl" -> "Apple, Inc. (AAPL)")

    # RETURN THE STOCK: NAME & TICKER, DESCRIPTION, PRICE from the function
    # calls the function to display the investment profile of player's chosen stock
    assigned_desc = assign_player_investment_profile(player_investment)

    # returns value of dictionary (returns the buying price of player)
    assigned_buyPrice = stocks_dict.get(player_investment_converted)

    # list out keys and values separately
    # buyName_list = list(stocks_dict.keys()) # Keys = Name
    buyPrice_list = list(stocks_dict.values()) # Values = Price

    # assigned_name = buyName_list.index(assigned_buyPrice)

    # CALCULATIONS FOR THE STOCK PRICE
    bought_shares = balance_cash / assigned_buyPrice


empty_line()

print(f"You have bought {bought_shares} shares of {player_investment_converted} at ${assigned_buyPrice}.")
print(assigned_desc)

time.sleep(10)

empty_line()

print(f"")
