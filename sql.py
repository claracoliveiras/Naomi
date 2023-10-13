import mysql.connector;

mydb = mysql.connector.connect(
    host= 'localhost',
    port=3306,
    user= 'root',
    database='naomi'
)

print(mydb)

mycursor = mydb.cursor()



sql = "INSERT INTO users (name, id, birthday, zodiac, timezone) VALUES (%s, %s, %s, %s, %s)"
val = ("Ana", 6, '2004-07-07 12:00:00', 'Cancer', '400' )
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

