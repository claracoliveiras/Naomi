from botinit import bot
from reminderSql import insertReminder, getRemindersByUserId, deleteReminderByName, deleteReminderById

@bot.command()
async def reminder(ctx, *args):
    setting = args[0].lower()
    userId = ctx.author.id
    reminders = getRemindersByUserId(userId)
    sampleArgs = ('set', 'edit', 'delete', 'list', 'search')
    # set - sets the reminder [.reminder set name YYYY-MM-DD]
    # edit - edits 
    # [.reminder edit id name [newname] 
    # [.reminder edit id date [newdate]]
    # delete - deletes the reminder based on the name .reminder delete [name]
    # list - lists all the reminders with their ids
    # search - searches the reminders
    # search between dates: [.reminder search [date1] [date2]]
    # search by name: [.reminder search [name]]
    # search by date: [.reminder search [date]]
    # search by today: [.reminder search today]

    if setting not in sampleArgs:
        return await ctx.message.channel.send("Invalid setting")
    #set
    elif setting == 'set':
        name = args[1]
        date = args[2]
        insertReminder(name, date, userId)
        reminders = getRemindersByUserId(userId)
        return await ctx.message.channel.send(f"Reminder set for date {date}")
    #edit
    elif setting == 'edit' and len(args) != 3:
        return await ctx.message.channel.send("Incorrect argument positioning or size.")
    elif setting == 'edit' and len(args) == 3:
        settingToEdit = args[1]
        settingUpdate = args[2]
        #keep writing this
    #delete
    elif setting == 'delete' and len(args) != 2:
        return await ctx.message.channel.send("Incorrect argument positioning or size.")
    elif setting == 'delete' and len(args) == 2:
        nameToDelete = args[1]
        deleteReminderByName(nameToDelete)
        return await ctx.message.channel.send(f"Reminder {nameToDelete} deleted.")
    

        
    