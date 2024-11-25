from Stock import Stock
from StockEntry import StockEntry
from datetime import datetime
import matplotlib.pyplot as plt

# Function for retrieving the latest stock data
def latest_data(stockName):
    print(stockName.data[-1])

# Function for retrieving stock data for a specific date
def specific_date_data(stockName, date_string):
    # date_string = input("Enter a date (YYYY-MM-DD): ")
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
def range_date_data(stockName, date_start_string, date_end_string):
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

def quarterly_data(stockName, year_string, quarter):
    if (quarter == 1):
        date_start_string = year_string + "-01-01"
        date_end_string = year_string + "-03-31"
        range_date_data(stockName, date_start_string, date_end_string)

    elif (quarter == 2):
        date_start_string = year_string + "-04-01"
        date_end_string = year_string + "-06-30"
        range_date_data(stockName, date_start_string, date_end_string)

    elif (quarter == 3):
        date_start_string = year_string + "-07-01"
        date_end_string = year_string + "-09-30"
        range_date_data(stockName, date_start_string, date_end_string)

    elif (quarter == 4):
        date_start_string = year_string + "-10-01"
        date_end_string = year_string + "-12-31"
        range_date_data(stockName, date_start_string, date_end_string)
    
    else:
        print("Please enter a valid quarter!")
        
def yearly_data(stockName, year_string):
    date_start_string = year_string + "-01-01"
    date_end_string = year_string + "-12-31"
    range_date_data(stockName, date_start_string, date_end_string)
    
# If user selects option 4 to view data on a specific date:
# specific_date_data()

# If user selects option 1 to view the latest data:
# latest_data()

# Data over a range of dates
# range_date_data("2014-12-12", "2015-12-12")

# quarterly_data("2014", 3)

# yearly_data("2014")