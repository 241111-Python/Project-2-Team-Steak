from Stock import Stock
from StockEntry import StockEntry
from datetime import datetime, timedelta
import json

'''
WHOLE GAME
'''
# def select_option(number):


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

print('''Welcome! Enter a number to access data on a specific stock!
        [1] - MSFT (Microsoft)
        [2] - AAPL (Apple)
        [3] - AMZN (Amazon)
        [4] - NFLX (Netflix)
        [5] - GOOG (Google)
        [6] - Input your own JSON stock data filepath''')

user_input = int(input()) - 1
listOfStocks = ["MSFT", "AAPL", "AMZN", "NFLX", "GOOG"]
# example: amzn = Stock(stockName)
globals()[listOfStocks[user_input].lower()] = Stock(listOfStocks[user_input])
stockName = globals()[listOfStocks[user_input].lower()]

data_source = f"./stock-data/{listOfStocks[user_input]}.json"
with open(data_source, "r") as file:
    for dict in json.load(file):
        #print(dict)
        stockName.addData(StockEntry(dict["date"], dict["open"], dict["high"], dict["low"], dict["close"], dict["volume"]))
'''
for x in stockName.data:
    print(x)

print(f"stockName: {listOfStocks[user_input]}")
'''
#print(globals()[listOfStocks[user_input].lower()].data[0])

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
def range_date_data():
    date_start_string = input("Enter a start date (YYYY-MM-DD): ")
    date_end_string = input("Enter an end date (YYYY-MM-DD): ")
    date_start_object = datetime.strptime(date_start_string, "%Y-%m-%d")
    date_end_object = datetime.strptime(date_end_string, "%Y-%m-%d")

    if  date_start_object.weekday() == 5:
        nearest_weekday_start = date_start_object - timedelta(days=1)
    elif date_start_object.weekday() == 6:
        nearest_weekday_start = date_start_object + timedelta(days=1)
    else:
        nearest_weekday_start = date_start_object
    date_start_string = nearest_weekday_start.strftime("%Y-%m-%d")

    if  date_end_object.weekday() == 5:
        nearest_weekday_end = date_end_object - timedelta(days=1)
    elif date_end_object.weekday() == 6:
        nearest_weekday_end = date_end_object + timedelta(days=1)
    else:
        nearest_weekday_end = date_end_object
    date_end_string = nearest_weekday_end.strftime("%Y-%m-%d")

    start_exists = False
    end_exists = False
    in_range = False

    data_string = ""
    for i in stockName.data:
        if (i.date == date_start_string):
            in_range = True
            start_exists = True
        if (in_range == True):
            data_string = data_string + str(i)
        if (i.date == date_end_string):
            in_range = False
            end_exists = True
            break
    print(data_string)


# If user selects option 4 to view data on a specific date:
# specific_date_data()

# If user selects option 1 to view the latest data:
# latest_data()

# Data over a range of dates
range_date_data()