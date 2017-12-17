class Stock:
    def __init__(self, chocolatestock, honeystock, marshmallowstock, chilipepperstock):
        self.chocolatestock = chocolatestock
        self.honeystock = honeystock
        self.marshmallowstock = marshmallowstock
        self.chilipepperstock = chilipepperstock

    def __del__(self):
        self.chocolatestock = None
        self.honeystock = None
        self.marshmallowstock = None
        self.chilipepperstock = None

    def getChocolatestock(self):
        return self.chocolatestock

    def getHoneystock(self):
        return self.honeystock

    def getMarshmallowstock(self):
        return self.marshmallowstock

    def getChilipepperstock(self):
        return self.chilipepperstock

    def setChocolatestock(self, chocolatestock):
        self.chocolatestock = chocolatestock

    def setHoneystock(self, honeystock):
        self.honeystock = honeystock

    def setMarshmallowstock(self, marshmallowstock):
        self.marshmallowstock = marshmallowstock

    def setChilipepperstock(self, chilipepperstock):
        self.chilipepperstock = chilipepperstock

    def stockOrder(self):
        deliveryTime = 0
        succes = True
        return deliveryTime, succes