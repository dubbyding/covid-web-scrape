from os.path import join
from platform import node
import firebase_admin
import os
from firebase_admin import db

class firebase_database_initializing():
    def __init__(self):
        if not firebase_admin._apps:
            current_location = os.path.dirname(os.path.realpath(__file__))
            cred_object = firebase_admin.credentials.Certificate(os.path.join(current_location,"file.json"))
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
        values = self.getDataOfNewCases()
        # print(values)
        if values is None:
            self.insert(node_address="/CovidMOHP/New_cases", json_file=json_file)
            return 0
        for key1, value1 in values.items():
            if(value1["New_cases"]==json_file["New_cases"]) and (value1["Date"]==json_file["Date"]):
                print("Value already exists in the database")
                return 0
        self.insert(node_address="/CovidMOHP/New_cases", json_f1ile=json_file)

    def insertIntoTotalCases(self, json_file):
        values = self.getDataOfTotalCases()
        # print(values)
        if values is None:
            self.insert(node_address="/CovidMOHP/Total_cases", json_file=json_file)
            return 0
        for key1, value1 in values.items():
            if(value1["Total_cases"]==json_file["Total_cases"]) and (value1["Date"]==json_file["Date"]):
                print("Value already exists in the database")
                return 0
        self.insert(node_address="/CovidMOHP/Total_cases", json_f1ile=json_file)
    
    def insertIntoTotalDeaths(self, json_file):
        values = self.getDataOfTotalDeaths()
        # print(values)
        if values is None:
            self.insert(node_address="/CovidMOHP/Total_deaths", json_file=json_file)
            return 0
        for key1, value1 in values.items():
            if(value1["Total_deaths"]==json_file["Total_deaths"]) and (value1["Date"]==json_file["Date"]):
                print("Value already exists in the database")
                return 0
        self.insert(node_address="/CovidMOHP/Total_deaths", json_f1ile=json_file)

    def insertIntoTotalRecovered(self, json_file):
        values = self.getDataOfTotalRecovered()
        # print(values)
        if values is None:
            self.insert(node_address="/CovidMOHP/Total_recovered", json_file=json_file)
            return 0
        for key1, value1 in values.items():
            if(value1["Total_recovered"]==json_file["Total_recovered"]) and (value1["Date"]==json_file["Date"]):
                print("Value already exists in the database")
                return 0
        self.insert(node_address="/CovidMOHP/Total_recovered", json_f1ile=json_file)

    def insert(self, node_address, json_file):
        print(json_file)
        ref = db.reference(node_address)
        ref.push().set(json_file)
    
    def getDataOfByDistrict(self):
        return self.getData(node_address="/CovidMOHP/By_district")
    
    def getDataOfNewCases(self):
        return self.getData(node_address="CovidMOHP/New_cases")
    
    def getDataOfTotalCases(self):
        return self.getData(node_address="CovidMOHP/Total_cases")
    
    def getDataOfTotalDeaths(self):
        return self.getData(node_address="CovidMOHP/Total_deaths")

    def getDataOfTotalRecovered(self):
        return self.getData(node_address="CovidMOHP/Total_recovered")

    def getData(self, node_address):
        ref = db.reference(node_address)
        value = ref.get()
        return value

