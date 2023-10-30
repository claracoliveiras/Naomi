import mysql.connector;

mydb = mysql.connector.connect(
    host= 'localhost',
    port=3306,
    user= 'root',
    database='naomi'
)

def getIds():
    idCursor = mydb.cursor()
    idCursor.execute("Select id FROM users")
    lista = idCursor.fetchall()
    listaIds = []
    for userId in lista:
        listaIds.append(userId[0])
    return listaIds

def insertUser(id):
    insertCursor = mydb.cursor()
    personInsert = "INSERT INTO users (name, id, birthday, zodiac, timezone) VALUES (%s, %s, %s, %s, %s)"
    val = (None, id, None, None, None)
    insertCursor.execute(personInsert, val)
    mydb.commit()
    print(insertCursor.rowcount, "record inserted.")

def fetchById(id):
    indvCursor = mydb.cursor()
    indvCursor.execute(f"SELECT * FROM users WHERE id ={id}")
    userById = indvCursor.fetchall()
    return userById

def alterUserById(id, setting, value):
    alterCursor = mydb.cursor()
    personUpdate = f"UPDATE users SET {setting} = %s WHERE id = %s"
    val = (value, id)
    alterCursor.execute(personUpdate, val)
    mydb.commit()
    print(alterCursor.rowcount, "records affected")

def deleteById(id):
    deleteCursor = mydb.cursor()
    deleteCursor.execute(f"DELETE FROM users WHERE id = {id}")
    mydb.commit()
    print(deleteCursor.rowcount, "record(s) deleted")
