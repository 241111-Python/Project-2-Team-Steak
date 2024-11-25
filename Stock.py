from datetime import datetime
from docx import Document
from docx.shared import Inches
import matplotlib.pyplot as plt

class Stock:
    def __init__(self, name):
        self.name = name
        self.data = []
        self.highest = {
            "open": float("-inf"),
            "high": float("-inf"),
            "low": float("-inf"),
            "close": float("-inf"),
            "volume": float("-inf"),
        }
        self.lowest = {
            "open": float("inf"),
            "high": float("inf"),
            "low": float("inf"),
            "close": float("inf"),
            "volume": float("inf"),
        }

    def addData(self, data):
        self.data.append(data)

    def latest_data(self):
        print(self.data[-1])

    def specific_date_data(self, date_string):
        #date_string = input("Enter a date (YYYY-MM-DD): ")
        date_object = datetime.strptime(date_string, "%Y-%m-%d")
        if (date_object.weekday() >= 5):
            print("Please enter a valid weekday! Stock markets close on weekends.")
            return
        else:
            exists = False
            for i in self.data:
                if (i.date == date_string):
                    exists = True
                    print(i)
                    break
            if (exists == False):
                print("The data is not currently available for this date!\n")

    def range_date_data(self, date_start_string, date_end_string, is_yearly = False):
        #date_start_string = input("Enter a start date (YYYY-MM-DD): ")
        #date_end_string = input("Enter an end date (YYYY-MM-DD): ")

        date_start_object = datetime.strptime(date_start_string, "%Y-%m-%d")
        date_end_object = datetime.strptime(date_end_string, "%Y-%m-%d")

        if (date_end_object < date_start_object):
            print("Please make sure your end date comes AFTER your start date!")
            return

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
        opening_prices = []

        data_string = ""
        for i in self.data:
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
                opening_prices.append(i.open)
                data_string = data_string + str(i)
            if ((i.date == date_end_string) or (date_object > date_end_object)):
                end_price = i.close
                in_range = False
                end_exists = True
                break
        if ((start_exists == False) or (end_exists == False)):
            print("Please enter valid start and end dates!")
            return

        print("Retrieving data from " + date_start_string + " to " + date_end_string)
        percentage_change = ((end_price - start_price)/start_price)*100
        avg_closing = total_closing/days
        avg_volume = total_volume/days
        # print(data_string)

        if (is_yearly == False):

            print("Lowest price is: " + str(lowest_price))
            print("Highest price is: " + str(highest_price))
            print("Average closing price is: " + str(avg_closing))
            print("Change in price is: " + str(percentage_change) + "%")
            print("Closing vs opening price is: " + str(close_open_diff))
            print("Average volume over this time period is: " + str(avg_volume))

            fig, ax1 = plt.subplots()

            ax1.plot(dates, closing_prices, color='b', label='Closing Price')
            ax1.set_xlabel('Date')
            ax1.set_ylabel('Closing Price', color='b')
            ax1.tick_params(axis='y', labelcolor='b')

            ax2 = ax1.twinx()
            ax2.plot(dates, opening_prices, color='r', label='Volume')
            ax2.set_ylabel('Opening Price', color='r')
            ax2.tick_params(axis='y', labelcolor='r')

            plt.xticks([dates[0], dates[-1]])
            if (percentage_change > 0):
                plt.title("Daily Stock Opening and Closing Prices( ↑" + str(round(percentage_change,2)) + "%)")
            else:
                plt.title("Daily Stock Opening and Closing Prices( ↓" + str(round(percentage_change,2)) + "%)")
            plt.xticks(rotation=45)
            plt.tight_layout()


        else:
            plt.figure(figsize=(10,5))
            plt.plot(dates, closing_prices, color='b', label='Closing Price')
            if (percentage_change > 0):
                plt.title("Daily Stock Opening and Closing Prices( ↑" + str(round(percentage_change,2)) + "%)")
            else:
                plt.title("Daily Stock Opening and Closing Prices( ↓" + str(round(percentage_change,2)) + "%)")
            plt.xlabel('Date')
            plt.ylabel('Closing Price')
            plt.xticks([dates[0], dates[-1]])
            plt.tight_layout()

        plt.savefig("graph.png")
        doc = Document()
        doc.add_paragraph("Lowest price is: " + str(lowest_price) + 
                          "\nHighest price is: " + str(highest_price) + 
                          "\nAverage closing price is: " + str(avg_closing) + 
                          "\nChange in price is: " + str(percentage_change) + 
                          "%\nClosing vs opening price is: " + str(close_open_diff) + 
                          "\nAverage volume over this time period is: " + str(avg_volume) + "\n")
        doc.add_picture('graph.png', width=Inches(6))
        doc.save('statistics.docx')
        # with open('statistics.docx', 'w') as file:
        #     file.write("Lowest price is: " + str(lowest_price) + "\n")
        #     file.write("Highest price is: " + str(highest_price) + "\n")
        #     file.write("Average closing price is: " + str(avg_closing) + "\n")
        #     file.write("Change in price is: " + str(percentage_change) + "%\n")
        #     file.write("Closing vs opening price is: " + str(close_open_diff) + "\n")
        #     file.write("Average volume over this time period is: " + str(avg_volume) + "\n")
        plt.show()

    def quarterly_data(self, year_string, quarter):
        if (quarter == 1):
            date_start_string = year_string + "-01-01"
            date_end_string = year_string + "-03-31"
            self.range_date_data(date_start_string, date_end_string)

        elif (quarter == 2):
            date_start_string = year_string + "-04-01"
            date_end_string = year_string + "-06-30"
            self.range_date_data(date_start_string, date_end_string)

        elif (quarter == 3):
            date_start_string = year_string + "-07-01"
            date_end_string = year_string + "-09-30"
            self.range_date_data(date_start_string, date_end_string)

        elif (quarter == 4):
            date_start_string = year_string + "-10-01"
            date_end_string = year_string + "-12-31"
            self.range_date_data(date_start_string, date_end_string)
        
        else:
            print("Please enter a valid quarter!")

    def yearly_data(self, year_string):
        date_start_string = year_string + "-01-01"
        date_end_string = year_string + "-12-31"
        self.range_date_data(date_start_string, date_end_string, True)

    def all_time_data(self):
        date_start_string = self.data[0].date
        date_end_string = self.data[-1].date
        self.range_date_data(date_start_string, date_end_string, True)