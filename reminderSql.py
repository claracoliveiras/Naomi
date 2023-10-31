import mysql.connector;
from sql import dbConnector;

def getRemindersByUserId(id):
    individualCursor = dbConnector.cursor()
    individualCursor.execute(f"SELECT * FROM reminders WHERE userId ={id}")
    remindersById = individualCursor.fetchall()
    remindersList = []
    for reminder in remindersById:
        remindersList.append(reminder)
    return remindersList

def getRemindersDates(id):
    individualCursor = dbConnector.cursor()
    individualCursor.execute(f"SELECT date FROM reminders WHERE userId ={id}")
    dates = individualCursor.fetchall()
    return [date[0] for date in dates]
    
def insertReminder(name, date, userId):
    insertCursor = dbConnector.cursor()
    reminderInsert = "INSERT INTO reminders (name, date, userId) VALUES (%s, %s, %s)"
    values = (name, date, userId)
    insertCursor.execute(reminderInsert, values)
    dbConnector.commit()
    print(insertCursor.rowcount, "record inserted.")

def deleteReminderByName(name):
    deleteCursor = dbConnector.cursor()
    deleteCursor.execute(f"DELETE FROM reminders WHERE name = '{name}'")
    dbConnector.commit()
    print(deleteCursor.rowcount, "record(s) deleted")

def deleteReminderById(reminderID):
    deleteCursor = dbConnector.cursor()
    deleteCursor.execute(f"DELETE FROM reminders WHERE reminderID = {reminderID}")
    dbConnector.commit()
    print(deleteCursor.rowcount, "record(s) deleted")
    
    # edit - edits 
    # [.reminder edit[0] id[1] name[2] [newname][3] 
    # [.reminder edit[0] id[1] name[2] [newdate][3]
def updateReminder(reminderID, setting, newValue):
    updateCursor = dbConnector.cursor()
    reminderUpdate = f"UPDATE reminders SET {setting} = %s WHERE reminderID = %s"
    val = (newValue, reminderID)
    updateCursor.execute(reminderUpdate, val)
    dbConnector.commit()
    print(updateCursor.rowcount, "records affected")
    
    
    
