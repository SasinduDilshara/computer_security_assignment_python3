from models.personal_data.personal_data_parent import PersonalData

class AdminData(PersonalData):
    def __init__(self, username, firstName, lastName, telephone , address):
        super().__init__(username, firstName, lastName, telephone , address)

    def __str__(self):
        return "username :- "+self.username+"\n"
                + "firstName :- "+self.firstName+"\n"
                +"lastName :- "+self.lastName+"\n"
                +"telephone :- "+self.telephone+"\n"
                +"address :- "+self.address+"\n"