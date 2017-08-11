class Room:
    def __init__(self, _name):
        self.name = _name
        self.users = []

    def addUser(self, _user):
        self.users.append(_user)

    def getUsers(self):
        return self.users
