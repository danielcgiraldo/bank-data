import json
from datetime import date

#TODO: Add some test to check that the data is correct

JSON_FILE = 'data/rates.json'
CDT_INTERVALS = ["90", "180", "360", "540"]

# Useful classes for storing data
class CDT:
    def __init__(self, bank, data={}):
        self.bank_id = bank
        self.data = data

    def add(self, obj_money):
        self.data[obj_money.left_value] = obj_money.days_dict

    def write(self):
        # Read current data
        with open(JSON_FILE, 'r') as f:
            current_data = json.load(f)

        # Save last update with current date
        self.data["last_update"] = str(date.today())

        if "CDT" not in current_data:
            current_data["CDT"] = {}
        
        # Add new data
        current_data["CDT"][self.bank_id] = self.data
        
        # Write new data
        with open(JSON_FILE, 'w') as f:
            json.dump(current_data, f, indent=4)


        

class CDTInterface:
    def __init__(self, left_value) -> None:
        self.left_value = left_value
        self.days_dict = {}

    def add(self, left_days, interest):
        if left_days in CDT_INTERVALS:
            self.days_dict[left_days] = interest

class FIC:
    def __init__(self, bank, data={}):
        self.bank_id = bank
        self.data = data

    def add(self, obj_fic):
        self.data[obj_fic.name] = obj_fic.dict

    def write(self):
        # Read current data
        with open(JSON_FILE, 'r') as f:
            current_data = json.load(f)

        # Save last update with current date
        self.data["last_update"] = str(date.today())

        if "FIC" not in current_data:
            current_data["FIC"] = {}
        
        # Add new data
        current_data["FIC"][self.bank_id] = self.data
        
        # Write new data
        with open(JSON_FILE, 'w') as f:
            json.dump(current_data, f, indent=4)

class FICInterface:
    def __init__(self, name) -> None:
        self.name = name
        self.dict = {}

    def add(self, period, result):
        self.dict[period] = result