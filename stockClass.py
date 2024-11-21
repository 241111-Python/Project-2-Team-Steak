class Stock:
    def __init__(self):
        self.date = []
        self.open = []
        self.high = []
        self.low = []
        self.close = []
        self.volume = []
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

    def addData(self, date, open, high, low, close, volume):
        args = { 
            "open": open,
            "high": high,
            "low": low,
            "close": close,
            "volume": volume,
        }
        self.date.append(date)
        self.open.append(open)
        self.high.append(high)
        self.low.append(low)
        self.close.append(close)
        self.volume.append(volume)
        for key, val in args.items():
            if self.highest[key] < val:
                self.highest[key] = val
            if self.lowest[key] > val:
                self.lowest[key] = val

    def latestData(self):
        return f"""Date: {self.date[-1]}
Open: {self.open[-1]}
High: {self.high[-1]}
Low: {self.low[-1]}
Close: {self.close[-1]}
Volume: {self.volume[-1]}"""


amzn = Stock()
amzn.addData("2013-02-08", 261.4, 265.25, 260.555, 261.95, 3879078)
print(amzn.latestData())
