from models.personal_data.personal_data_parent import PersonalData

class PatientData(PersonalData):
    def __init__(self, username, firstName, lastName, telephone , address,age,special_notes):
        super().__init__(username, firstName, lastName, telephone , address)
        self.age = age
        self.special_notes = special_notes

    def __str__(self):
        a =  "username :- "+self.username+"\n"
        a += "firstName :- "+self.firstName+"\n"
        a += "lastName :- "+self.lastName+"\n"
        a += "telephone :- "+self.telephone+"\n"
        a += "address :- "+self.address+"\n"
        a += "age :- "+self.age+"\n"
        a += "special_notes :- "+self.special_notes
        return a