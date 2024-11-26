from Stock import Stock
from StockEntry import StockEntry
import json
import argparse
import datetime
import re

                                                            #STEAK N STAKES


parser = argparse.ArgumentParser(description="Stock Analyzer Tool")                                                                                         #Created Parsing arguments to allow users to automate or semi-automate the script depending on their needs
parser.add_argument("--filePath", type=str, help="Path to your custom JSON stock data file", required=False)                                                #First OPTIONAL parsing argument      filepath    ex: "python .\main.py --filePath stock-data\AAL.json"
parser.add_argument("--defaultInput", type=int, help="Input to select ALL stock data", required=False)                                                      #Second OPTIONAL parsing argument  defaultInput   ex: ".\main.py --filePath stock-data\AAL.json --defaultInput 1"
args = parser.parse_args()

question_Prompt = """
=========================================================
Enter a number to select one of the following
    [1] - View Latest trading price
    [2] - View all stock data       
    [3] - View all stock data on a SPECIFIC date 
    [4] - View all stock data from __ to __
    [5] - View stock data from a specific year at Q? (QUARTERLY)
    [6] - View stock data for a specific year (ANNUALLY)
========================================================="""
listOfStocks = ["MSFT", "AAPL", "AMZN", "NFLX", "GOOG"]

def select_option(stock, number):                                                                                                                          #Logic for implementing the statistics menu
    while True:                                                                                                                                            #Depending on which number was input is which function from Stock.py will be called
        if number == 1:
            print(stock.latest_data())
        elif number == 2:
            stock.all_time_data()
        elif number == 3:
            date_string = input("Enter a date (YYYY-MM-DD): ")
            stock.specific_date_data(date_string)
        elif number == 4:
            date_start_string = input("Enter a start date (YYYY-MM-DD): ")
            date_end_string = input("Enter an end date (YYYY-MM-DD): ")
            stock.range_date_data(date_start_string, date_end_string)
        elif number == 5:
            year_input = input("Enter year: ")
            quarter_input = int(input("Enter quarter (1-4): "))
            stock.quarterly_data(year_input, quarter_input)
        elif number == 6:
            year_input = input("Enter year: ")
            stock.yearly_data(year_input)
        else:
            print("Invalid Option: Try Again")
            return True  # Return to previous menu

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


def load_stock_data(file_path, stock_name="Custom Stock"):                                                                                                 #Function to load JSON files if user wants to provide their own 
    stock = Stock(stock_name)
    try:
        with open(file_path, "r") as file:
            for dict_entry in json.load(file):
                stock.addData(
                    StockEntry(
                        dict_entry["date"],
                        dict_entry["open"],
                        dict_entry["high"],
                        dict_entry["low"],
                        dict_entry["close"],
                        dict_entry["volume"],
                    )
                )
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None 
    except json.JSONDecodeError:                                                                                                                         #This error is if the JSON is not formatted properly
        print(f"Error: Failed to parse JSON from {file_path}")
        return None
    return stock


def main_menu():                                                                                                                                        #Logic for the main menu function
    while True:
        print(
            """Welcome! Enter a number to access data on a specific stock!
            [1] - MSFT (Microsoft)
            [2] - AAPL (Apple)
            [3] - AMZN (Amazon)
            [4] - NTFX (Netflix)
            [5] - GOOG (Google)
            [0] - Exit Program
            """
        )
        try:
            user_input = int(input()) - 1

            if user_input == -1:
                print("Exiting the program. Goodbye!")
                break

            elif 0 <= user_input <= 4:
                data_source = f"./stock-data/{listOfStocks[user_input]}.json"
                stock = load_stock_data(data_source, listOfStocks[user_input])
                if stock:
                    access_secondary_menu(stock)

            elif user_input == 5:  # Custom input during execution
                file_path = input("Enter the filepath to your JSON stock data: ").strip()
                stock = load_stock_data(file_path)
                if stock:
                    access_secondary_menu(stock)
            else:
                print("Invalid input. Please try again.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")


def access_secondary_menu(stock, file_path = None):                                                                                                 #Function to skip to the secondary menu if a separate JSON file is provided by the user (Used if parsing args are provided)                                           
    if args.defaultInput == 1:                                                                                                                      #Will automatically run option 1 from the stats menu if the input field is also provided as an args (Reference line 10)
        print(stock.latest_data())
        if file_path:
            with open(file_path + "/latest_data.txt", "a") as file:
                file.write("Stock: " + stock.name + "\n")
                file.write(str(stock.latest_data()))
                file.write("Date: " + str(datetime.date.today()) + "\n\n")
        else:
            with open("latest_data.txt", "a") as file:
                file.write("Stock: " + stock.name + "\n")
                file.write(str(stock.latest_data()))
                file.write("Date: " + str(datetime.date.today()) + "\n\n")
        exit(0)
    
    while True:
        print(question_Prompt)
        try:
            option = int(input("Enter your choice: "))
            if option == 0:
                print("Returning to Stock Selection Menu...")
                break
            if not select_option(stock, option):
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")


if args.filePath:                                                                                                                                 #This block will load data from a user inputted JSON file and automatically format it so it can be called through the crontab as well
    print(f"Loading custom JSON stock data from: {args.filePath}")                                                                                #The stock value will be set to the data from the file and the second menu function will be called 
    stock = None
    if args.filePath[:5] == "/mnt/":
        stock_name = re.split(r'[\/.]', args.filePath)
        stock = load_stock_data(args.filePath, stock_name[-2])
        if stock:
            access_secondary_menu(stock, "/mnt/d/Visual Studio Codes/Revature/Week 2/Project-2-Team-Steak")
    else:
        stock_name = re.split(r'[\\.]', args.filePath)
        stock = load_stock_data(args.filePath, stock_name[1])
        if stock:
            access_secondary_menu(stock)
else:
    main_menu()
