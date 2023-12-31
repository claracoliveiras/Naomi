from botinit import bot
from discord import Embed
from reminderSql import insertReminder, getRemindersByUserId, deleteReminderByName, deleteReminderById, updateReminder

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
    elif setting == 'edit' and len(args) != 4:
        return await ctx.message.channel.send("Incorrect argument positioning or size.")
    elif setting == 'edit' and len(args) == 4:
        reminderID = args[1]
        settingToEdit = args[2]
        settingUpdateValue = args[3]
        updateReminder(reminderID, settingToEdit, settingUpdateValue)
        return await ctx.message.channel.send(f"Reminder {settingToEdit} updated.")
    #delete
    elif setting == 'delete' and len(args) != 2:
        return await ctx.message.channel.send("Incorrect argument positioning or size.")
    elif setting == 'delete' and len(args) == 2:
        nameToDelete = args[1]
        deleteReminderByName(nameToDelete)
        return await ctx.message.channel.send(f"Reminder {nameToDelete} deleted.")
    elif setting == 'list':
        list_embed = Embed(title ="Reminders", description="Description", color=0x034e95)
        formatted_data = []
        for i, item in enumerate(reminders, start=1):
            formatted_data.append(f"{i}. ID: {item[0]}, Name: {item[1]}, Date: {item[2]}")

        formatted_string = "\n".join(formatted_data)
        list_embed.description = formatted_string
        return await ctx.message.channel.send(embed=list_embed)
        
        
    

        
    