class Worker:
    def __init__(self, id, firstname, lastname, workload):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.workload = workload
        self.occupied = False

    def __del__(self):
        self.id = None
        self.firstname = None
        self.lastname = None
        self.workload = None
        self.occupied = None

    def getId(self):
        return self.id

    def getName(self):
        return self.firstname, self.lastname

    def getWorkload(self):
        return self.workload

    def getOccupied(self):
        return self.occupied

    def setOccupied(self, status):
        self.occupied = status