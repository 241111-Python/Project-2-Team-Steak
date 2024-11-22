# import stockClass
import json

from datetime import datetime

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
            user_input = int(input("Enter your choice: "))
            if user_input == 0:
                print("Exiting the program. Goodbye!")
                break  # Exit the main menu
            elif 1 <= user_input <= 5:
                stock_names = ["Microsoft", "Apple", "Amazon", "Netflix", "Google"]
                print(f"\nAccessing {stock_names[user_input - 1]}...")

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
