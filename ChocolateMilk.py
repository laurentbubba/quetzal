class ChocolateMilk:
    def __init__(self, id, price):
        self.id = id
        self.price = price
        self.ingredients = None

    def __del__(self):
        self.id = None
        self.price = None
        self.ingredients = None

    def getPrice(self):
        return self.price

    def getId(self):
        return self.id

    def addIngredient(self):


    def returnWorkload(self):
