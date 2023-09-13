import json
from datetime import date

#TODO: Add some test to check that the data is correct

JSON_FILE = 'data.json'

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
        
        # Add new data
        current_data[self.bank_id] = self.data
        
        # Write new data
        with open(JSON_FILE, 'w') as f:
            json.dump(current_data, f, indent=4)


        

class MoneyInterface:
    def __init__(self, left_value) -> None:
        self.left_value = left_value
        self.days_dict = {}

    def add(self, left_days, interest):
        self.days_dict[left_days] = interest
