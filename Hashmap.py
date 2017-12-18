from LinkedList_hmap import LinkedList

class Hashmap:
    v = []
    max_size = 0
    myType = 0

    #Empty constructor
    def __init__(self):
        return None

    def createHashmap(self, myType, max_size):
        self.myType = myType
        self.max_size = max_size
        self.v = [None] * max_size

        return True
    
    def begin(self):
        i = 0
        if self.myType == 3:
            while self.v[i] == None:
                i+=1
            return self.v[i].first()

        while self.v[i] == None:
            i+=1
        return self.v[i]

    def end(self):
        i = len(self.v) -1
        if self.myType == 3:
            while self.v[i] == None:
                i-=1
            return self.v[i].last()

        while self.v[i] == None:
            if i == 0: return None
            i-=1
        return self.v[i]

    def insert(self, toAdd, key=None):
        if key == None: key = toAdd

        if self.hash(key) > self.max_size:
            return insert(key % self.max_size, toAdd) 
        
        if self.myType == 3:
            #Seperate chaining
            if self.v[self.hash(key)] == None:
                l = LinkedList()
                l.append(toAdd)
                self.v[self.hash(key)] = l
            else:
                self.v[self.hash(key)].append(toAdd)

        if self.v[self.hash(key)] != None:
            i = self.hash(key)
            #Linear probing
            if self.myType == 0:
                while (self.v[i] != None):
                    i+=1
                self.v[i] = toAdd

            if self.myType == 1:
                #Quadratic probing
                while(self.v[i] != None):
                    i+=1
                    i = i ** 2 % self.max_size
                self.v[i] = toAdd
        
        self.v[self.hash(key)] = toAdd
        return True

    def erase(self, toErase, d=None):
        if d == None: d = toErase

        if self.myType == 3:
            self.v[self.hash(toErase)].deleteByValue(d)
            return True
               
               

        del self.v[self.hash(toErase)]
        return True

    def findByHash(self, h):
        
        return self.v[h]

    def hash(self, key):
        return (key % 15) -3

    def findByValue(self, value):
        if self.myType == 3:
            return self.v[self.hash(value)].findByValue(value)

        return self.v[self.hash(value)]

    def print(self):
        if self.myType == 3:
            for i in self.v:
                if i == None:
                    print(None)
                else:
                    i.print()
        else:
            print(self.v)

