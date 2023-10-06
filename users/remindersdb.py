import json

reminder_entries = {}

def readJson():
    with open('users/reminders.json', 'r') as f:
        data = json.load(f)
    return data

def writeJson(new_entries): 
    with open('users/reminders.json', 'w') as f:
        json.dump(new_entries, f, indent=4)