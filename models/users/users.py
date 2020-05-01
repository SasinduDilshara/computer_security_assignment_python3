from abc import ABC

class User(ABC):
    '''
    Abstract class for users.
    '''
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def getPassword(self):
        return self.__password
    def setPassword(self,password):
        self.__password = password
        

