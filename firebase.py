from os.path import join
import firebase_admin
import os
from firebase_admin import db

class firebase_database_initializing():
    def __init__(self):
        if not firebase_admin._apps:
            current_location = os.path.dirname(os.path.realpath(__file__))
            cred_object = firebase_admin.credentials.Certificate(os.path.join(current_location,"rugged-coil-292608-firebase-adminsdk-rl5m0-773bda45bb.json"))
            databaseURL = "https://rugged-coil-292608-default-rtdb.firebaseio.com/"
            default_app = firebase_admin.initialize_app(cred_object, {
                'databaseURL':databaseURL
                })

    def insertIntoByDistrict(self, json_file):
        values = self.getDataOfByDistrict()
        # print(values)
        if values is None:
            self.insert(node_address="/CovidMOHP/By_district", json_file=json_file)
            return 0
        for key1, value1 in values.items():
            # print(value1)
            if(value1["location"]==json_file["location"]):
                if (value1["number_of_female"] == json_file["number_of_female"]) and (value1["number_of_male"] == json_file["number_of_male"]):
                    print("Value already exists in the Database")
                    return 0
        self.insert(node_address="/CovidMOHP/By_district", json_file=json_file)
            
    
    def insertIntoNewCases(self, json_file):
        self.insert(node_address="/CovidMOHP/New_cases", json_file=json_file)
    


    def insert(self, node_address, json_file):
        print(json_file)
        ref = db.reference(node_address)
        ref.push().set(json_file)
    
    def getDataOfByDistrict(self):
        return self.getData(node_address="/CovidMOHP/By_district")
    
    def getDataOfNewCases(self):
        return self.getData(node_address="CovidMOHP/New_cases")

    def getData(self, node_address):
        ref = db.reference(node_address)
        value = ref.get()
        return value

# Testing
if __name__ == "__main__": 
    print("in")
    fdb = firebase_database_initializing()
    values = fdb.getDataOfByDistrict()
    for key1, value1 in values.items():
        if value1["location"] == json_file["location"] and value1["number_of_female"] == json_file["number_of_female"] and value1["number_of_male"] == json_file["number_of_female"]:
            print("Value already exists in the Database")
        else:
            pass