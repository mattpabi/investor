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
    empty_line()
    empty_line()


# DISPLAY THE RULES OF THE GAME
def display_rules():
    print("+-------------------------------------------------  ABOUT THE GAME  -------------------------------------------------+")
    print("|                                                                                                                    |")
    print("|    This game is an investing simulation that enables players to learn the risks and rewards involved in the        |")
    print("|    decision-making and risk-taking of financial markets.                                                           |")
    print("|                                                                                                                    |")
    print("|    You will start off with a balance of $100,000 to invest and grow your money through your chosen asset(s).       |")
    print("|    Your goal is to win the challenge by growing your money to $1,000,000.                                          |")
    print("|                                                                                                                    |")
    print("|                                                                                                                    |")
    print("|    *NOTE: $1,000,000 in your cash balance, NOT in your portfolio value (you MUST SELL to WIN the game).*           |")
    print("|                                                                                                                    |")
    print("|                                                                                                                    |")
    print("|    A fully randomised set of economic events will be presented to you, and you will be given the option to         |")
    print("|    buy, hold, or sell.                                                                                             |")
    print("|                                                                                                                    |")
    print("|    In order to win the game, you must search for clues in the news, read between the lines, and play some          |")
    print("|    hunches. The game will end once you have beat the challenge, or run out of money. You may type QUIT at          |")
    print("|    any time to leave the game.                                                                                     |")
    print("|                                                                                                                    |")
    print("+--------------------------------------------------------------------------------------------------------------------+")


# PRESS ANY KEY TO CONTINUE OR TYPE "QUIT" TO QUIT
def continue_or_quit():
    CorQ = input("Press enter or return to continue, or type 'QUIT' to quit the game.")
    CorQ_lower = CorQ.lower()

    if CorQ_lower == "quit":
        print("Come back next time when you are ready, see you soon.")
        time.sleep(5)
        quit()
    
    time.sleep(1)


# STOCKS DICTIONARY
stocks_dict = {
    "Apple, Inc. (AAPL)" : "168.49",
    "Microsoft Corp. (MSFT)" : "287.02",
    "Alphabet, Inc. (GOOGL)" : "118.84",
    "Amazon.com, Inc. (AMZN)" : "140.64",
    "Tesla, Inc. (TSLA)" : "859.89",
    "Berkshire Hathaway (BRK-B)" : "296.47",
    "Meta Platforms, Inc. (META)" : "177.49",
    "Netflix, Inc. (NFLX)" : "242.70"
}


# TO MAINTAIN TABLE MARGINS, THIS FUNCTION WILL COUNT THE CHARACTERS IN THE PRICE AND ADD SPACES ACCORDINGLY
def investment_options_space_counter(stock):
    if len(str(stock)) == 10:
        space = r""
    
    elif len(str(stock)) == 9:
        space = r" "
    
    elif len(str(stock)) == 8:
        space = r"  "
    
    elif len(str(stock)) == 7:
        space = r"   "
    
    elif len(str(stock)) == 6:
        space = r"    "

    elif len(str(stock)) == 5:
        space = r"     "
    
    elif len(str(stock)) == 4:
        space = r"      "
    
    return space


# DISPLAY INVESTMENT OPTIONS
def display_stocks():
    # STOCK PRICES (FOR EASE OF USE WHEN PRINTING)
    stockPrice_apple = float(stocks_dict.get("Apple, Inc. (AAPL)"))
    stockPrice_microsoft = float(stocks_dict.get("Microsoft Corp. (MSFT)"))
    stockPrice_alphabet = float(stocks_dict.get("Alphabet, Inc. (GOOGL)"))
    stockPrice_amazon = float(stocks_dict.get("Amazon.com, Inc. (AMZN)"))
    stockPrice_tesla = float(stocks_dict.get("Tesla, Inc. (TSLA)"))
    stockPrice_berkshire = float(stocks_dict.get("Berkshire Hathaway (BRK-B)"))
    stockPrice_meta = float(stocks_dict.get("Meta Platforms, Inc. (META)"))
    stockPrice_netflix = float(stocks_dict.get("Netflix, Inc. (NFLX)"))
    
    print(f"+-------------------------  INVESTMENT OPTIONS  ------------------------+")
    print(f"|                                                                       |")
    print(f"+--- Ticker ----- Company ---------------------------------- Price -----+")
    print(f"|    AAPL         Apple, Inc.                                ${format(stockPrice_apple, '.2f')}{investment_options_space_counter(format(stockPrice_apple, '.2f'))}|")
    print(f"|    MSFT         Microsoft Corp.                            ${format(stockPrice_microsoft, '.2f')}{investment_options_space_counter(format(stockPrice_microsoft, '.2f'))}|")
    print(f"|    GOOGL        Alphabet, Inc. (Google)                    ${format(stockPrice_alphabet, '.2f')}{investment_options_space_counter(format(stockPrice_alphabet, '.2f'))}|")
    print(f"|    AMZN         Amazon.com, Inc.                           ${format(stockPrice_amazon, '.2f')}{investment_options_space_counter(format(stockPrice_amazon, '.2f'))}|")
    print(f"|    TSLA         Tesla, Inc.                                ${format(stockPrice_tesla, '.2f')}{investment_options_space_counter(format(stockPrice_tesla, '.2f'))}|")
    print(f"|    BRK-B        Berkshire Hathaway, Inc.                   ${format(stockPrice_berkshire, '.2f')}{investment_options_space_counter(format(stockPrice_berkshire, '.2f'))}|")
    print(f"|    META         Meta Platforms, Inc. (FKA Facebook)        ${format(stockPrice_meta, '.2f')}{investment_options_space_counter(format(stockPrice_meta, '.2f'))}|")
    print(f"|    NFLX         Netflix, Inc.                              ${format(stockPrice_netflix, '.2f')}{investment_options_space_counter(format(stockPrice_netflix, '.2f'))}|")
    print(f"|                                                                       |")  
    print(f"+-----------------------------------------------------------------------+")


# STOCK KEYWORDS (CHECK IF INPUT IS IN THIS LIST)
stocks_keywords_list = ["aapl", "apple, inc.", "apple", "msft", "microsoft corp.", "microsoft", "googl", "alphabet", "alphabet, inc.", "google", "amzn", "amazon.com", "amazon.com, inc.", "amazon", "tsla", "tesla, inc.", "tesla", "brk-b", "berkshire hathaway, inc.", "berkshire hathaway", "berkshire", "meta", "meta platforms, inc.", "meta platforms", "meta", "nflx", "netflix, inc.", "netflix"]


# STOCK CHOICE INPUT CONVERTER - uses 'keywords' to lessen errors on user's end
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
    
    elif investment_choice_lower == "amzn" or investment_choice_lower == "amazon.com" or investment_choice_lower == "amazon.com, inc." or investment_choice_lower == "amazon":
        investment_choice = "Amazon.com, Inc. (AMZN)"
        return investment_choice

    elif investment_choice_lower == "tsla" or investment_choice_lower == "tesla, inc." or investment_choice_lower == "tesla":
        investment_choice = "Tesla, Inc. (TSLA)"
        return investment_choice

    elif investment_choice_lower == "brk-b" or investment_choice_lower == "berkshire hathaway, inc." or investment_choice_lower == "berkshire" or investment_choice_lower == "berkshire hathaway":
        investment_choice = "Berkshire Hathaway (BRK-B)"
        return investment_choice

    elif investment_choice_lower == "meta" or investment_choice_lower == "meta platforms, inc." or investment_choice_lower == "meta platforms" or investment_choice_lower == "meta":
        investment_choice = "Meta Platforms, Inc. (META)"
        return investment_choice

    elif investment_choice_lower == "nflx" or investment_choice_lower == "netflix, inc." or investment_choice_lower == "netflix":
        investment_choice = "Netflix, Inc. (NFLX)"
        return investment_choice


# PLAYER INVESTMENT PROFILES - descriptions of companies
def assign_player_investment_profile(investment_choice):
    
    if investment_choice == "Apple, Inc. (AAPL)":
        investment_choice_profile = "Apple, Inc. engages in the design, manufacture, and sale of smartphones, personal computers, tablets, wearables and accessories, and other varieties of related services."
        return investment_choice_profile

    elif investment_choice == "Microsoft Corp. (MSFT)":
        investment_choice_profile = "Microsoft Corp. engages in the development and support of software, services, devices, and solutions."
        return investment_choice_profile

    elif investment_choice == "Alphabet, Inc. (GOOGL)":
        investment_choice_profile = "Alphabet, Inc. is a holding company, which engages in the business of acquisition and operation of different companies, such as its main internet products: ads, Android, Chrome, hardware, Google Cloud, Google Maps, Google Play, Search, and YouTube."
        return investment_choice_profile
    
    elif investment_choice == "Amazon.com, Inc. (AMZN)":
        investment_choice_profile = "Amazon.com, Inc. is a multinational technology company, which engages in the provision of online retail shopping services."
        return investment_choice_profile

    elif investment_choice == "Tesla, Inc. (TSLA)":
        investment_choice_profile = "Tesla, Inc. engages in the design, development, manufacture, and sale of fully electric vehicles and energy generation and storage systems."
        return investment_choice_profile

    elif investment_choice == "Berkshire Hathaway (BRK-B)":
        investment_choice_profile = "Berkshire Hathaway, Inc. engages in the provision of property and casualty insurance and reinsurance, utilities and energy, freight rail transportation, finance, manufacturing, and retailing services."
        return investment_choice_profile

    elif investment_choice == "Meta Platforms, Inc. (META)":
        investment_choice_profile = "Meta Platforms, Inc. engages in the development of social media applications. It builds technology that helps people connect, find communities, and grow businesses."
        return investment_choice_profile

    elif investment_choice == "Netflix, Inc. (NFLX)":
        investment_choice_profile = "Netflix, Inc. operates as a streaming entertainment service company. The firm provides subscription service streaming movies and television episodes over the internet."
        return investment_choice_profile


######## INITIALISE PORTFOLIO DASHBOARD VARIABLES

# positions
pf_positions_open = 0
pf_positions_asset = "N/A"
pf_postions_shares = 0

# prices and values
pf_price_current = 0
pf_price_current_total_value = 0
pf_price_when_bought = 0
pf_price_total_acquisition_cost = 0

# balances
pf_balance_cash = 100000 #starting cash
pf_balance_investments = 0 #starting value of investments
pf_balance_investments_pnl = 0 #starting + or - of investments


# DISPLAY PLAYER PORTFOLIO
def display_player_portfolio():
    print(f"______________________________  PORTFOLIO  ______________________________\n")
    print(f"   Open positions                             {int(pf_positions_open)}\n")

    print(f"   Invested asset                             {pf_positions_asset}")
    print(f"   Number of shares                           {format(pf_postions_shares, '.2f')}\n")
    
    print(f"   ($) Current price                          {format(pf_price_current, '.2f')}")
    print(f"   ($) Current total value                    {format(pf_price_current_total_value, '.2f')}")
    print(f"   ($) Price when bought                      {format(pf_price_when_bought, '.2f')}")
    print(f"   ($) Total acquisition cost                 {format(pf_price_total_acquisition_cost, '.2f')}\n")

    print(f"   ($) Current cash on hand                   {format(abs(pf_balance_cash), '.2f')}")
    print(f"   ($) Current value of investments           {format(pf_balance_investments, '.2f')}")
    print(f"   ($) Profit / Loss on open position         {format(pf_balance_investments_pnl, '.2f')} \n")
    print("__________________________________________________________________________")


# GENERATE RANDOM EVENTS AND SCENARIOS
def random_generator_news(asset):
    random_Days = random.randint(1, 20) #randomly generates days to determine whether news is breaking news or not

    # sudden breaking news
    if random_Days < 6:
        random_Event_good = [f"BREAKING: {asset} has signed a striking deal with tech giant for $1 billion.", f"BREAKING: The CEO of {asset} hinted at a potential merger with world-renowned industry giant.", f"BREAKING: {asset} to discuss stock buyback in next shareholders meeting.", f"BREAKING: 'The end of Quantitative Tightening brings forth Quantitative Easing' says Fed chairman Jerome Powell."]
        random_Event_bad = [f"BREAKING: The current CEO of {asset} is stepping down and may discountinue operations.", f"BREAKING: The databases of {asset} have been hacked: personal details of private investors and/or users have been breached - CEO confirms", f"BREAKING: Financial data provided by {asset} has been proven to be false, including Financial Statements and Balance Sheets, company insiders confirm.", f"BREAKING: Fed chairman Jerome Powell announces a 100bps interest rate hike, suprising forecasters by 25bps."]
 
        random_Event_sentiment_pick = random.randint(0, 1)
 
        if random_Event_sentiment_pick == 0:
            random_Event_pick = random.randint(0, (len(random_Event_bad)-1))
            random_Event_picked = random_Event_bad[random_Event_pick]
            random_Event_sentiment = "bad"

        elif random_Event_sentiment_pick == 1:
            random_Event_pick = random.randint(0, (len(random_Event_good)-1))
            random_Event_picked = random_Event_good[random_Event_pick]
            random_Event_sentiment = "good"

    else:
        random_Event_good = [f"Earnings Call: Revenues of {asset} exceed analyst expectations by 20%.", f"Ray Dalio's billion-dollar hedge fund Bridgewater has bought {asset} stock.", f"U.S. Government to inject $1 Trillion into the market through bonds to incentivise spending, the S&P 500 and Dow 30 indexes both see a 10% recovery.", f"CPI and Core CPI prints 100bps less than analyst expectations, 'inflation is over' says economists."]
        random_Event_bad = [f"Earnings call: Revenues of {asset} miss analyst expectations by 15%.", f"Institutions dump {asset} stock ahead of anticipated slump in earnings.", f"Economists warns of potential recession with high inflation, and 'too little too late' interest rate hikes.", f"Oil and food prices rise amid high inflation.", f"U.S. Federal Reserve raises interest rates by 200 bps for the first time since the 1900s."]

        random_Event_sentiment_pick = random.randint(0, 1)
 
        if random_Event_sentiment_pick == 0:
            random_Event_pick = random.randint(0, (len(random_Event_bad)-1))
            random_Event_picked = random_Event_bad[random_Event_pick]
            random_Event_sentiment = "bad"

        elif random_Event_sentiment_pick == 1:
            random_Event_pick = random.randint(0, (len(random_Event_good)-1))
            random_Event_picked = random_Event_good[random_Event_pick]
            random_Event_sentiment = "good"

    return random_Event_picked, random_Event_sentiment # returns news, and sentiment


# GENERATE RANDOM PRICE ACTION BASED ON SENTIMENT OF RANDOM NEWS
def random_generator_prices(asset_price, sentiment):
    percentage_number = round(random.uniform(15, 55), 2)
    percentage_decimal = percentage_number / 100

    percentage_print = str(percentage_number) + "%"
    
    if sentiment == "good":
        new_asset_price = round(asset_price * (1 + percentage_decimal),2)

    elif sentiment == "bad":
        new_asset_price = round(asset_price * (1 - percentage_decimal),2)

    return new_asset_price, percentage_print


def news_generator(player_investment_converted):
    start_new_window()

    print("""
                                                   /$$                                 /$$ /$$ /$$                              
                                                  | $$                                | $$| $$|__/                              
 /$$$$$$$   /$$$$$$  /$$  /$$  /$$  /$$$$$$$      | $$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$$| $$ /$$ /$$$$$$$   /$$$$$$   /$$$$$$$
| $$__  $$ /$$__  $$| $$ | $$ | $$ /$$_____/      | $$__  $$ /$$__  $$ |____  $$ /$$__  $$| $$| $$| $$__  $$ /$$__  $$ /$$_____/
| $$  \ $$| $$$$$$$$| $$ | $$ | $$|  $$$$$$       | $$  \ $$| $$$$$$$$  /$$$$$$$| $$  | $$| $$| $$| $$  \ $$| $$$$$$$$|  $$$$$$ 
| $$  | $$| $$_____/| $$ | $$ | $$ \____  $$      | $$  | $$| $$_____/ /$$__  $$| $$  | $$| $$| $$| $$  | $$| $$_____/ \____  $$
| $$  | $$|  $$$$$$$|  $$$$$/$$$$/ /$$$$$$$/      | $$  | $$|  $$$$$$$|  $$$$$$$|  $$$$$$$| $$| $$| $$  | $$|  $$$$$$$ /$$$$$$$/
|__/  |__/ \_______/ \_____/\___/ |_______/       |__/  |__/ \_______/ \_______/ \_______/|__/|__/|__/  |__/ \_______/|_______/ 
""")

    time.sleep(1)

    empty_line()

    #print the news and sentiment
    news, sentiment = random_generator_news(player_investment_converted)
    print(f"News        {news}")
    print(f"Sentiment   {sentiment.title()}")

    time.sleep(1)

    empty_line()
    
    assigned_buyPrice = pf_price_when_bought
    
    new_asset_price, percentage_print = random_generator_prices(float(stocks_dict.get(player_investment_converted)), sentiment)

    pf_price_current = new_asset_price

    #print a table showing the asset's price movement
    print(f"_______________ {player_investment_converted} _______________\n")

    print(f"($) Buy price                           {assigned_buyPrice}")
    print(f"($) Current price                       {new_asset_price}")
    print(f"(%) Percentage move since last price    {percentage_print}")

    price_difference =  round(new_asset_price, 2) - round(assigned_buyPrice, 2)
    print(f"($) Price difference since bought       {format(price_difference, '.2f')}")

    underscore_counter = 0
    for i in range(len(player_investment_converted)):
        underscore_counter = underscore_counter + 1

    underscores = "_" * (underscore_counter + 2) #to make the table formatting dynamic and adaptable to any kind of string-length
    print(f"_______________{underscores}_______________")


    ########## UPDATES STOCK PRICE ##########

    #stocks_dict[player_investment_converted] = new_asset_price
    stocks_dict.update({player_investment_converted:new_asset_price})


# PLAYER USERNAME EASTER EGG
player_username_easter_egg_dict = {
    "steve jobs": "Apple",
    "bill gates": "Microsoft",
    "larry page": "Google",
    "sergey brin": "Google",
    "jeff bezos": "Amazon",
    "elon musk": "Tesla",
    "warren buffett": "Berkshire Hathaway",
    "charlie munger": "Berkshire Hathaway",
    "mark zuckerberg": "Facebook",
    "reed hastings": "Netflix",
    "marc randolph":"Netflix",
    }

player_username_easter_egg_list = list(player_username_easter_egg_dict.keys())


########## INTRO ##########


clear_terminal()

username = input("Hello there! Please enter your desired username: ")

if username.lower() in player_username_easter_egg_list:

    print("\n> Congratulations! You have just found the game's easter egg!")

    player_username_easter_egg_company = player_username_easter_egg_dict.get(username.lower())
    print(f"\nOh hi there {username}! I did not expect to see you today...")
    print(f"Have fun playing this game, hopefully you'll find success here just like you did at {player_username_easter_egg_company}!")



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
    time.sleep(10)
    quit()

print("> Let's begin")

print("\nFor the best experience, please make sure that you are playing this game in your native terminal, in fullscreen.")
print("This game was coded in Python 3.10, running this game in prior Python versions may result in glitches or bugs that disrupt the gaming experience.")

empty_line()
continue_or_quit()



########## DISPLAY RULES ##########

start_new_window()

display_rules()

empty_line()
continue_or_quit()



########## DISPLLAY INVESTMENT OPTIONS ##########

############ LOOP FROM HERE

while pf_balance_cash < 1000000 and pf_balance_cash >= 0:
    if pf_positions_open == 0:
        start_new_window()

        display_stocks()

        # DISPLAY PLAYER PORTFOLIO
        empty_line()

        display_player_portfolio()

        # INPUT INVESTMENT
        empty_line()
        player_investment = input("Please input the your desired stock to invest in: ")


        if player_investment.lower() in stocks_keywords_list:
            player_investment_converted = player_investment_choice_converter(player_investment)

        else:
            if player_investment.lower() != "quit":

                # loop in case the user's first answer is invalid
                while player_investment.lower() != "quit":
                    player_investment = input("Please input a valid stock ticker/name: ")

                    if player_investment.lower() in stocks_keywords_list:
                        player_investment_converted = player_investment_choice_converter(player_investment)
                        break

                    elif player_investment.lower() == "quit":
                        print("Come back next time when you are ready, see you soon.")
            
            elif player_investment.lower() == "quit":
                print("Come back next time when you are ready, see you soon.")
        
        # checks if player can afford any stocks, quit the game if they can't
        affordable_counter = 0
        for share_price in stocks_dict:
            if float(pf_balance_cash) >= float(stocks_dict[share_price]):
                affordable_counter = affordable_counter + 1
            else:
                pass
        
        if affordable_counter == 0:
            print("Sorry you have insufficient funds to buy any shares of any listed stock.")
            time.sleep(0.5)
            print("""
 /$$                                        
| $$                                        
| $$  /$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$ 
| $$ /$$__  $$ /$$_____/ /$$__  $$ /$$__  $$
| $$| $$  \ $$|  $$$$$$ | $$$$$$$$| $$  \__/
| $$| $$  | $$ \____  $$| $$_____/| $$      
| $$|  $$$$$$/ /$$$$$$$/|  $$$$$$$| $$      
|__/ \______/ |_______/  \_______/|__/      
""")
            time.sleep(10)
            quit()


        if float(pf_balance_cash) < float(stocks_dict.get(player_investment_converted)):
            print("Sorry you do not have enough funds to purchase the stock.\n")
            continue_or_quit()
            continue




        # PRINT ONCE INVESTMENT INPUT IS VALID
        print("> Processing transaction...")
        time.sleep(1)
        print("> Success!")
        time.sleep(1)

        # RETRIEVE STOCK PRICE
        assigned_buyPrice = float(stocks_dict.get(player_investment_converted))

        # CALCULATE SHARES BOUGHT
        bought_shares = float(pf_balance_cash) / float(assigned_buyPrice)

        # RETRIEVE STOCK DESCRIPTION
        assigned_desc = assign_player_investment_profile(player_investment_converted)

        empty_line()

        print(f"You have bought {int(bought_shares)} shares of {player_investment_converted} at ${format(assigned_buyPrice, '.2f')}.")
        print(assigned_desc)

        time.sleep(1)
    
        ########## UPDATES PLAYER VALUES ##########

        # positions
        pf_positions_open = 1
        pf_positions_asset = player_investment_converted
        pf_postions_shares = bought_shares

        # prices and values
        pf_price_current = assigned_buyPrice
        pf_price_current_total_value = assigned_buyPrice * pf_postions_shares
        pf_price_when_bought = assigned_buyPrice
        pf_price_total_acquisition_cost = pf_price_when_bought * pf_postions_shares

        # balances
        pf_balance_cash = pf_balance_cash - pf_price_total_acquisition_cost #starting cash
        pf_balance_investments = pf_price_current_total_value # value of investments
        pf_balance_investments_pnl = pf_price_total_acquisition_cost -  pf_price_current_total_value # + or - of investments


        empty_line()
        display_player_portfolio()


        empty_line()
        continue_or_quit()

        news_generator(player_investment_converted)

    else:

        ######### UPDATES PLAYER VALUES ##########
        # positions
        pf_positions_open = 1
        pf_positions_asset = player_investment_converted
        pf_postions_shares = bought_shares

        # prices and values
        pf_price_current = float(stocks_dict.get(player_investment_converted))
        pf_price_current_total_value = pf_price_current * pf_postions_shares
        pf_price_when_bought = assigned_buyPrice
        pf_price_total_acquisition_cost = pf_price_when_bought * pf_postions_shares

        # balances
        #pf_balance_cash = pf_balance_cash - pf_price_total_acquisition_cost #starting cash
        pf_balance_investments = pf_price_current_total_value # value of investments
        pf_balance_investments_pnl = pf_price_current_total_value - pf_price_total_acquisition_cost# + or - of investments

        empty_line()
        empty_line()
        display_player_portfolio()

        empty_line()
        
        buy_sell_hold = input("""
Considering recent news, would you like to:
(a) Sell your shares, exiting your position
(b) Hold your position, take no action

*You may not buy more shares as you have a cash balance of $0.00

Please input your choice: """)

        if buy_sell_hold.lower() == "a" or buy_sell_hold.lower() == "sell":
            buy_sell_hold_Choice = "sell"
            # balances
            pf_balance_cash = pf_price_current_total_value
            pf_balance_investments = 0 #starting value of investments
            pf_balance_investments_pnl = 0 #starting + or - of investments

            # positions
            pf_positions_open = 0
            pf_positions_asset = "N/A"
            pf_postions_shares = 0

            # prices and values
            pf_price_current = 0
            pf_price_current_total_value = 0
            pf_price_when_bought = 0
            pf_price_total_acquisition_cost = 0

        elif buy_sell_hold.lower() == "b" or buy_sell_hold.lower() == "hold":
            buy_sell_hold_Choice = "hold"            

        else:
            if buy_sell_hold.lower() != "quit":
                
                # while loop to keep prompting user for valid input, in the event first answer is invalid
                while buy_sell_hold.lower() != "quit":

                    buy_sell_hold = input("Please input a valid choice: ")
                    
                    if buy_sell_hold.lower() == "a" or buy_sell_hold.lower() == "sell":
                        buy_sell_hold_Choice = "sell"
                        # balances
                        pf_balance_cash = pf_price_current_total_value
                        pf_balance_investments = 0 #starting value of investments
                        pf_balance_investments_pnl = 0 #starting + or - of investments

                        # positions
                        pf_positions_open = 0
                        pf_positions_asset = "N/A"
                        pf_postions_shares = 0

                        # prices and values
                        pf_price_current = 0
                        pf_price_current_total_value = 0
                        pf_price_when_bought = 0
                        pf_price_total_acquisition_cost = 0
                        break

                    elif buy_sell_hold.lower() == "b" or buy_sell_hold.lower() == "hold":
                        buy_sell_hold_Choice = "hold"
                        break

                    elif buy_sell_hold.lower() == "quit":
                        print("See you soon.")
                        quit()

            elif buy_sell_hold.lower() == "quit":
                print("See you soon.")
                quit()

            
        print(f"> So, {username}, you have chosen to {buy_sell_hold_Choice}.")

        empty_line()
        continue_or_quit()

        if buy_sell_hold_Choice.lower() == "hold":
            news_generator(pf_positions_asset)     


    ####################
    if pf_balance_cash >= 1000000:
        clear_terminal()
        print(f"\nCongratulations, {username}, you are the winner.\n")
        time.sleep(0.5)
        print("""
    /$$          /$$      /$$ /$$$$$$ /$$   /$$ /$$   /$$ /$$$$$$$$ /$$$$$$$           /$$   
  /$$$$$$       | $$  /$ | $$|_  $$_/| $$$ | $$| $$$ | $$| $$_____/| $$__  $$        /$$$$$$ 
 /$$__  $$      | $$ /$$$| $$  | $$  | $$$$| $$| $$$$| $$| $$      | $$  \ $$       /$$__  $$
| $$  \__/      | $$/$$ $$ $$  | $$  | $$ $$ $$| $$ $$ $$| $$$$$   | $$$$$$$/      | $$  \__/
|  $$$$$$       | $$$$_  $$$$  | $$  | $$  $$$$| $$  $$$$| $$__/   | $$__  $$      |  $$$$$$ 
 \____  $$      | $$$/ \  $$$  | $$  | $$\  $$$| $$\  $$$| $$      | $$  \ $$       \____  $$
 /$$  \ $$      | $$/   \  $$ /$$$$$$| $$ \  $$| $$ \  $$| $$$$$$$$| $$  | $$       /$$  \ $$
|  $$$$$$/      |__/     \__/|______/|__/  \__/|__/  \__/|________/|__/  |__/      |  $$$$$$/
 \_  $$_/                                                                           \_  $$_/ 
   \__/                                                                               \__/                                
""")
        time.sleep(0.5)
        print("""
Have fun being rich :), hope to see you soon
- anon
""")
        time.sleep(0.5)
        display_player_portfolio()
        time.sleep(1.5)
        continue_or_quit()
        quit()
        break
