# import stockClass
import json

# appl = stockClass("/fileForApple")
# amzn = stockClass()
# goog = stockClass()

# data_source = "./stock-data/AAPL_DATA.json"
# with open(data_source, "r") as file:
#     for dict in json.load(file):
#         appl.addData()

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
        [4] - NTFX (Netflix)
        [5] - GOOG (Google)''')

user_input = int(input())

if user_input == 1:
    print("")
    print("Accessing Microsoft...")
    print(question_Prompt)
elif user_input == 2:
    print("")
    print("Accessing Apple...")
    print(question_Prompt)
elif user_input == 3:
    print("")
    print("Accessing Amazon...")
    print(question_Prompt)
elif user_input == 4:
    print("")
    print("Accessing Netflix...")
    print(question_Prompt)
elif user_input == 5:
    print("")
    print("Accessing Google...")
    print(question_Prompt)
else:
    print("Incorrect Input!...")    


'''
store something in txt file?
'''
