from json import dump, load

entries = {} # this is everyone's data, its also the same in db.json

def write_db(data):
    with open('db.json', 'w') as f:
        dump(data, f, indent=4)

def read_db():
    with open('db.json', 'r') as f:
        data = load(f)
    return data


def update_entries():
    print(entries)
    write_db(entries)
