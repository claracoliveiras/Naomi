import json

def write_db(data):
    with open('db.json', 'w') as f:
        json.dump(data, f, indent=4)

def read_db():
    with open('db.json', 'r') as f:
        data = json.load(f)
    return data

all_data = None

