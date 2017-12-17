class Honey:
    def __init__(self, price, expiredate):
        self.price = price
        self.expiredate = expiredate

    def __del__(self):
        self.price = None
        self.expiredate = None

    def getPrice(self):
        return self.price

    def getExpiredate(self):
        return self.expiredate