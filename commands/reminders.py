from botinit import bot
from users.remindersdb import readJson, writeJson, reminder_entries
import util

reminder_entries = readJson()


@bot.command()
async def dailyReminder(ctx, *args):
    sampleArgs = ['set']

    userId = str(ctx.author.id)
    setting = args[0]
    name = args[1]
    date = util.time_String_Parser_Pos(args)

    if userId not in reminder_entries:
        reminder_entries[userId] = {}

    if setting in sampleArgs:
        reminder_entries[userId].update({
            name: {
                "date": date
            }
        })
        writeJson(reminder_entries)

        return await ctx.message.channel.send('Reminder set!')
