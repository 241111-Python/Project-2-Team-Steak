class StockEntry:
    def __init__(self, date, open, high, low, close, volume):
        self.date = date
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume

    def __str__(self):
        return (f"Stock Entry on {self.date}:\n"
                f"Open: {self.open}, High: {self.high}, Low: {self.low}, Close: {self.close}, Volume: {self.volume}\n")
