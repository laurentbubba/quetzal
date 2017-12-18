class ChocolateShot:
    def __init__(self, type, expiredate):
        self.type = type
        self.price = 1
        self.expiredate = expiredate

    def __del__(self):
        self.type = None
        self.price = None
        self.expiredate = None

    def getType(self):
        return self.type

    def getPrice(self):
        return self.price

    def getExpiredate(self):
        return self.expiredate