import numpy, random
import matplotlib.pyplot as plt

class Stock(object):
    def __init__(self, price, distribution):
        self.price = price
        self.history = [price]
        self.distribution = distribution # Risk
        self.lastChange = 0
    def setPrice(self, price):
        self.price = price
        self.history.append(price)
    def getPrice(self):
        return self.price
    def makeMove(self, marketBias, momentum):
        oldPrice = self.price
        baseMove = self.distribution() + marketBias
        self.price = self.price * (1.0 + baseMove)
        if momentum:
            self.price = self.price + random.gauss(.5, .5)*(self.lastChange)
        if self.price < 0.01:
            self.price = 0.0
        self.history.append(self.price)
        self.lastChange = oldPrice - self.price
    def showHistory(self, figNum):
        plt.figure(figNum)
        plt.plot(self.history)
        plt.title('Closing Prices Test ' + str(figNum))  
        plt.xlabel('Day')
        plt.ylabel('Price')      

def unitTestStock():
    numStks = 20
    numDays = 100
    bias = 0.0
    momentum = True 
    stks1 = []
    stks2 = []
    def runSim(stocks, fig, momentum):
        mean = 0.0
        for stock in stocks:
            for d in range(numDays):
                stock.makeMove(bias, momentum)
            stock.showHistory(fig)
            mean += stock.getPrice()
        mean = mean/float(numStks) 
        plt.axhline(mean)
    for i in range(numStks):
        volatility = random.uniform(0, 0.2)
        d1 = lambda: random.uniform(-volatility, volatility)
        d2 = lambda: random.gauss(0.0, volatility/2.0)
        stks1.append(Stock(100.0, d1))
        stks2.append(Stock(100.0, d2))
    runSim(stks1, 1, momentum)
    runSim(stks2, 2, momentum)

unitTestStock()
plt.show()
