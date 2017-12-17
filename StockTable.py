from CircularLinkedList import CircularLinkedList

class StockTable:
    def __init__(self):
        self.table = CircularLinkedList()

    def __del__(self):
        self.table = None

    def isEmpty(self):
        return self.table.isEmpty()

    def getLength(self):
        return self.table.getLength()

    def tableInsert(self, newitem):
        self.table.insert(0, newitem)
        return self.table.sort()    #Sort not yet implemented in Circular Linked List

    def tableDelete(self, index):  #Add ability to delete when expiredate is given
        return self.table.delete(index)

    def tableRetrieve(self, index): #Add ability to retrieve when expiredate is given
        return self.table.retrieve(index)

    def traverseTable(self):
        traverseList = []
        for i in range(0, self.table.getLength()):
            traverseList.append(self.tableRetrieve(i))
