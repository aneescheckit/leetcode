class StockSpanner:

    def __init__(self):
        self.stocks = [(0, 0)]
        self.callIndex = 0
        

    def next(self, price: int) -> int:
        self.callIndex += 1
        
        while len(self.stocks) > 1 and self.stocks[-1][1] <= price:
            self.stocks.pop()

        index, p = self.stocks[-1]

        self.stocks.append([self.callIndex, price])

        return self.callIndex - index


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
