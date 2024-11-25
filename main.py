from Stock import Stock
from StockEntry import StockEntry
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
            print(
                "View stock price change percentage from __ to __ (ANNUALLY, QUARTERLY)"
            )
        elif number == 6:
            print("You want to Return stock price change percentage (ALL TIME)")
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
    [1] - View LATEST stock data 
    [2] - View LOWEST trading price
    [3] - View HIGHEST trading price
    [4] - View all stock data on a SPECIFIC date 
    [5] - View stock price change percentage from __ to __ (ANNUALLY, QUARTERLY)
    [6] - Return stock price change percentage (ALL TIME)
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
                print(
                    """
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
                    """
                )
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
