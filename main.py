import stockClass
import json

appl = stockClass()
amzn = stockClass()
goog = stockClass()

data_source = "./stock-data/AAPL_DATA.json"
with open(data_source, "r") as file:
    for dict in json.load(file):
        appl.addData()

'''
WHOLE GAME
'''

'''
store something in txt file?
'''
