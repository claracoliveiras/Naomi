from db import all_data, read_db


def main():
    all_data = {}
    db_data = read_db()
    for key in db_data.keys():
        all_data[int(key)] = db_data[key]
    print(all_data)

main()