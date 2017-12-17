class Node():
    def __init__(self, item, next = None):
        self.item = item
        self.next = next

    def getItem(self):
        return self.item

    def getNext(self):
        return self.next

    def setNext(self, next):
        self.next = next