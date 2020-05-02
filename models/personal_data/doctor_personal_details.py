from models.personal_data.personal_data_parent import PersonalData

class DoctorData(PersonalData):
    def __init__(self, username, firstName, lastName, telephone , address,doc_id,nic):
        super().__init__(username, firstName, lastName, telephone , address)
        self.doc_id = doc_id
        self.nic = nic

    def __str__(self):
        
        a =  "username :- "+self.username+"\n"
        a += "firstName :- "+self.firstName+"\n"
        a += "lastName :- "+self.lastName+"\n"
        a += "telephone :- "+self.telephone+"\n"
        a += "address :- "+self.address+"\n"
        a += "nic :- "+self.nic+"\n"
        a += "doc_id :- "+self.doc_id
        return a