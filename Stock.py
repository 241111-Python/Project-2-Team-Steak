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
