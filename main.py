from Stock import Stock
from StockEntry import StockEntry
import json


def select_option(number):
    default_Response = True

    while default_Response:
        if number == 1:
            stockName.latest_data()
        elif number == 2:
            stockName.all_time_data()
        elif number == 3:
            date_string = input("Enter a date (YYYY-MM-DD): ")
            stockName.specific_date_data(date_string)
        elif number == 4:
            date_start_string = input("Enter a start date (YYYY-MM-DD): ")
            date_end_string = input("Enter an end date (YYYY-MM-DD): ")
            stockName.range_date_data(date_start_string, date_end_string)
        elif number == 5:
            year_input = input("Enter year: ")
            quarter_input = int(input("Enter quarter (1-4): "))
            stockName.quarterly_data(year_input, quarter_input)
        elif number == 6:
            year_input = input("Enter year: ")
            stockName.yearly_data(year_input)
        else:
            print("Invalid Option: Try Again")
            return True  # Return to previous menu

        # Ask if the user wants to continue
        user_Response = (
            input("Would you like to view another statistic? (y/n): ").strip().lower()
        )

        if user_Response == "n":
            print("Returning to the main menu...")
            return False  # Exit and return to main menu
        elif user_Response == "y":
            print("Returning to the selection menu...")
            return True  # Signal to restart menu selection
        else:
            print("Invalid Input. Returning to the main menu...")
            return False


question_Prompt_2 = "Would you like to view another statistic? (y/n)"


question_Prompt = """
=========================================================
Enter a number to select one of the following
    [1] - View Latest trading price
    [2] - View all stock data          # print day 1 and latest data
    [3] - View all stock data on a SPECIFIC date 
    [4] - View all stock data from __ to __
    [5] - View stock data from a specific year at Q? (QUARTERLY)
    [6] - View stock data for a specific year (ANNUALLY)
========================================================="""


while True:  # Main menu loop
    print(
        """Welcome! Enter a number to access data on a specific stock!
        [1] - MSFT (Microsoft)
        [2] - AAPL (Apple)
        [3] - AMZN (Amazon)
        [4] - NTFX (Netflix)
        [5] - GOOG (Google)
        [6] - Input your own JSON stock data filepath
        [0] - Exit Program
        """
    )

    try:
        user_input = int(input()) - 1
        listOfStocks = ["MSFT", "AAPL", "AMZN", "NFLX", "GOOG"]
        stockName = Stock(listOfStocks[user_input])

        data_source = f"./stock-data/{listOfStocks[user_input]}.json"
        with open(data_source, "r") as file:
            for dict in json.load(file):
                # print(dict)
                stockName.addData(
                    StockEntry(
                        dict["date"],
                        dict["open"],
                        dict["high"],
                        dict["low"],
                        dict["close"],
                        dict["volume"],
                    )
                )

        if user_input == -1:
            print("Exiting the program. Goodbye!")
            break  # Exit the main menu
        elif 0 <= user_input <= 4:
            print(f"\nAccessing {listOfStocks[user_input]}...")
            while True:  # Submenu loop for statistics
                print(question_Prompt)
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


"""
store something in txt file?
"""
# test = Stock("NFLX")
# with open("./stock-data/NFLX.json", "r") as file:
#     for dict in json.load(file):
#         test.addData(
#             StockEntry(
#                 dict["date"],
#                 dict["open"],
#                 dict["high"],
#                 dict["low"],
#                 dict["close"],
#                 dict["volume"],
#             )
#         )
# test.yearly_data("2015")
