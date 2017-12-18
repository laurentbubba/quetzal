class Node:
    #Constructor
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    #Constructor
    def __init__(self):
        self.head = None
        return

    #Add to end of list
    def append(self, d):
        new_node = Node(d)

        if self.head == None:
            self.head = new_node
            return

        last = self.head
        while(last.next):
            last = last.next

        last.next = new_node

    #Insert after specific node
    def insertAfter(self, previous, d):
        if previous == None:
            return

        new_node = Node(d)
        new_node.next = previous.next
        previous.next = new_node

    #Return data at specific key
    #Specific to Hashmap
    def keyToData(self, key):
        temp = self.head
        while (temp):
            if temp.data[0] == key:
                return temp.data[1]

            temp = temp.next
    
    #Inserting data and mapping to a key
    #Specific to Hashmap
    def mapDataToKey(self, key, data):
        temp = self.head
        while (temp):
            if temp.data[0] == None:
                temp.data[0] = key
                temp.data[1] = data
                return

            temp = temp.next

    #Emptying a node by value
    #Specific to Hashmap
    def deleteByValue(self, v):
        temp = self.head
        while (temp):
            if temp.data == v:
                temp.data = None
            temp = temp.next

    def findByValue(self, v):
        temp = self.head
        while (temp):
            if temp.data == v:
                return v
            temp = temp.next

    def last(self):
        temp = self.head
        while(temp):
            data = temp.data
            temp = temp.next

        return data

    def first(self):
        return self.head.data

    def print(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next
