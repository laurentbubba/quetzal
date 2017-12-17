class User:
    def __init__(self, id, firstname, lastname, mailadress):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.mailadress = mailadress

    def __del__(self):
        self.id = None
        self.firstname = None
        self.lastname = None
        self.mailadress = None

    def getId(self):
        return self.id

    def getName(self):
        return self.firstname, self.lastname

    def getMailadress(self):
        return self.mailadress