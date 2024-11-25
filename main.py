from Stock import Stock
from StockEntry import StockEntry
from datetime import datetime
import matplotlib.pyplot as plt
import json


def select_option(number):
    default_Response = True

    while default_Response:
        if number == 1:
            for x in stockName.data:
                print(x)  
            print(f"stockName: {listOfStocks[user_input]}")
        elif number == 2:
            print("You want to View LOWEST trading price")
        elif number == 3:
            print("You want to View HIGHEST trading price")
        elif number == 4:
            print("You want to View all stock data on a SPECIFIC date")
        elif number == 5:
            print("View stock price change percentage from __ to __ (ANNUALLY, QUARTERLY)")
        elif number == 6:
            print("You want to Return stock price change percentage (ALL TIME)")
        else:
            print("Invalid Option: Try Again")
            return True  # Return to previous menu

        # Ask if the user wants to continue
        user_Response = input("Would you like to view another statistic? (y/n): ").strip().lower()

        if user_Response == 'n':
            print("Returning to the main menu...")
            return False  # Exit and return to main menu
        elif user_Response == 'y':
            print("Returning to the selection menu...")
            return True  # Signal to restart menu selection
        else:
            print("Invalid Input. Returning to the main menu...")
            return False

    
question_Prompt_2 = "Would you like to view another statistic? (y/n)"


question_Prompt = '''
=========================================================
Enter a number to select one of the following
    [1] - View LATEST stock data 
    [2] - View LOWEST trading price
    [3] - View HIGHEST trading price
    [4] - View all stock data on a SPECIFIC date 
    [5] - View stock price change percentage from __ to __ (ANNUALLY, QUARTERLY)
    [6] - Return stock price change percentage (ALL TIME)
========================================================='''


while True:  # Main menu loop
        print('''Welcome! Enter a number to access data on a specific stock!
        [1] - MSFT (Microsoft)
        [2] - AAPL (Apple)
        [3] - AMZN (Amazon)
        [4] - NTFX (Netflix)
        [5] - GOOG (Google)
        [6] - Input your own JSON stock data filepath
        [0] - Exit Program
        ''')

        try:
            user_input = int(input()) - 1
            listOfStocks = ["MSFT", "AAPL", "AMZN", "NFLX", "GOOG"]

            globals()[listOfStocks[user_input].lower()] = Stock(listOfStocks[user_input])
            stockName = globals()[listOfStocks[user_input].lower()]

            data_source = f"./stock-data/{listOfStocks[user_input]}.json"
            with open(data_source, "r") as file:
                for dict in json.load(file):
                    # print(dict)
                    stockName.addData(StockEntry(dict["date"], dict["open"], dict["high"], dict["low"], dict["close"], dict["volume"]))


            if user_input == -1:
                print("Exiting the program. Goodbye!")
                break  # Exit the main menu
            elif 0 <= user_input <= 4:
                print(f"\nAccessing {listOfStocks[user_input]}...")
                while True:  # Submenu loop for statistics
                    print('''
=========================================================
Enter a number to select one of the following:
    [1] - View LATEST stock data 
    [2] - View LOWEST trading price
    [3] - View HIGHEST trading price
    [4] - View all stock data on a SPECIFIC date 
    [5] - View stock price change percentage from __ to __ (ANNUALLY, QUARTERLY)
    [6] - Return stock price change percentage (ALL TIME)
    [0] - Go Back to the Stock Selection Menu
=========================================================
                    ''')
                    try:
                        option = int(input("Enter your choice: "))
                        if option == 0:
                            print("Returning to Stock Selection Menu...")
                            break  # Exit submenu to return to stock selection menu
                        if not select_option(option):
                            break  # Exit submenu to main menu
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")

            elif user_input == 6:
                print("\nYou chose to input your own JSON stock data filepath.")
                # Add your custom JSON handling here
            else:
                print("Incorrect Input! Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


'''
store something in txt file?
'''

# Function for retrieving the latest stock data
def latest_data():
    print(stockName.data[-1])

# Function for retrieving stock data for a specific date
def specific_date_data():
    date_string = input("Enter a date (YYYY-MM-DD): ")
    date_object = datetime.strptime(date_string, "%Y-%m-%d")
    if (date_object.weekday() >= 5):
        print("Please enter a valid weekday! Stock markets close on weekends.")
        specific_date_data()
    else:
        exists = False
        for i in stockName.data:
            if (i.date == date_string):
                exists = True
                print(i)
                break
        if (exists == False):
            print("The data is not currently available for this date!\n")

# Function for retrieving the data for a range of dates
def range_date_data(date_start_string, date_end_string):
    #date_start_string = input("Enter a start date (YYYY-MM-DD): ")
    #date_end_string = input("Enter an end date (YYYY-MM-DD): ")

    date_start_object = datetime.strptime(date_start_string, "%Y-%m-%d")
    date_end_object = datetime.strptime(date_end_string, "%Y-%m-%d")

    start_exists = False
    end_exists = False
    in_range = False

    start_price = 0
    end_price = 0

    total_closing = 0
    total_volume = 0
    days = 0

    close_open_diff = 0

    lowest_price = 9999999
    highest_price = 0

    dates = []
    closing_prices = []

    data_string = ""
    for i in stockName.data:
        date_object = datetime.strptime(i.date, "%Y-%m-%d")
        if ((i.date == date_start_string) or ((date_object > date_start_object) and (start_exists == False))):
            start_price = i.close
            in_range = True
            start_exists = True
        if (in_range == True):
            if (i.low < lowest_price):
                lowest_price = i.low
            if (i.high > highest_price):
                highest_price = i.high
            total_closing += i.close
            total_volume += i.volume
            days += 1
            close_open_diff += (i.close - i.open)
            dates.append(i.date)
            closing_prices.append(i.close)
            data_string = data_string + str(i)
        if ((i.date == date_end_string) or (date_object > date_end_object)):
            end_price = i.close
            in_range = False
            end_exists = True
            break

    print("Retrieving data from " + date_start_string + " to " + date_end_string)
    percentage_change = ((end_price - start_price)/start_price)*100
    avg_closing = total_closing/days
    avg_volume = total_volume/days
    print(data_string)

    print("Lowest price is: " + str(lowest_price))
    print("Highest price is: " + str(highest_price))
    print("Average closing price is: " + str(avg_closing))
    print("Change in price is: " + str(percentage_change) + "%")
    print("Closing vs opening price is: " + str(close_open_diff))
    print("Average volume over this time period is: " + str(avg_volume))

    plt.figure(figsize=(10,5))
    plt.plot(dates, closing_prices, color='b', label='Closing Price')
    plt.title('Stock Closing Prices')
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.xticks([dates[0], dates[-1]])
    plt.tight_layout()
    plt.show()

def quarterly_data(year_string, quarter):
    if (quarter == 1):
        date_start_string = year_string + "-01-01"
        date_end_string = year_string + "-03-31"
        range_date_data(date_start_string, date_end_string)

    elif (quarter == 2):
        date_start_string = year_string + "-04-01"
        date_end_string = year_string + "-06-30"
        range_date_data(date_start_string, date_end_string)

    elif (quarter == 3):
        date_start_string = year_string + "-07-01"
        date_end_string = year_string + "-09-30"
        range_date_data(date_start_string, date_end_string)

    elif (quarter == 4):
        date_start_string = year_string + "-10-01"
        date_end_string = year_string + "-12-31"
        range_date_data(date_start_string, date_end_string)
    
    else:
        print("Please enter a valid quarter!")
        
def yearly_data(year_string):
    date_start_string = year_string + "-01-01"
    date_end_string = year_string + "-12-31"
    range_date_data(date_start_string, date_end_string)
    
# If user selects option 4 to view data on a specific date:
# specific_date_data()

# If user selects option 1 to view the latest data:
# latest_data()

# Data over a range of dates
# range_date_data("2014-12-12", "2015-12-12")

# quarterly_data("2014", 3)

# yearly_data("2014")

