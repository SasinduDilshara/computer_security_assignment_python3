from abc import ABC


class PersonalData(ABC):
    def __init__(self, username, firstName, lastName, telephone , address):
        self.username = username
        self.firstName = firstName
        self.lastName = lastName
        self.telephone = telephone
        self.address = address
    
    def __str__(self):
        a =  "username :- "+self.username+"\n"
        a += "firstName :- "+self.firstName+"\n"
        a += "lastName :- "+self.lastName+"\n"
        a += "telephone :- "+self.telephone+"\n"
        a += "address :- "+self.address+"\n"
        return a
    
