from Stock import Stock
from StockEntry import StockEntry
import json

stockName = input("Enter stock name: ")
# example: amzn = Stock(stockName)
globals()[stockName.lower()] = Stock(stockName) 

data_source = f"./stock-data/{stockName}.json"
with open(data_source, "r") as file:
    for dict in json.load(file):
        print(dict)
        globals()[stockName.lower()].addData(StockEntry(dict["date"], dict["open"], dict["high"], dict["low"], dict["close"], dict["volume"]))

for x in globals()[stockName.lower()].data:
    print(x)

print(f"stockName: {stockName}")