class Marshmallow:
    def __init__(self, expiredate):
        self.price = 0.75
        self.expiredate = expiredate

    def __del__(self):
        self.price = None
        self.expiredate = None

    def getPrice(self):
        return self.price

    def getExpiredate(self):
        return self.expiredate