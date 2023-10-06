from botinit import bot
import parsedatetime
from datetime import datetime
from random import randint
from users.db import readJson, writeJson, new_entries

new_entries = readJson()

def browhat_message(): 
    browhat = ("Well, you should greet me first!", "What?", "Didnt your mom give you basic education?")
    
    return browhat[0]

@bot.command()
async def config(ctx, *args):

    sampleArgs = ('name', 'zodiac', 'birthday')
    sampleZodiacs = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces']
    userId = str(ctx.author.id)
    setting = args[0]
    value = args[1]
    
    if setting == 'birthday':
        if userId not in new_entries:
            new_entries[userId] = {}
        cal = parsedatetime.Calendar()
        time_struct, status = cal.parse(parse_Birthday_String(args))
        dt = datetime(*time_struct[:6])
        
        value = int(dt.timestamp())

        new_entries[userId][setting] = value
        writeJson(new_entries)
        return await ctx.message.channel.send(f'{setting.capitalize()} set!')
    
    if setting == 'zodiac':
        if value not in sampleZodiacs:
            return await ctx.message.channel.send('This is not a zodiacal sign!')
        
    if setting in sampleArgs:
        if userId not in new_entries:
            new_entries[userId] = {}
        new_entries[userId][setting] = value
        writeJson(new_entries)
        return await ctx.message.channel.send(f'{setting.capitalize()} set!')
    await ctx.message.channel.send('Property doesnt exist')

def parse_Birthday_String(args):
    new_string = ""
    for i in range(1, len(args)):
        new_string += " " + args[i]
    return new_string