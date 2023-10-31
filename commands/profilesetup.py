from botinit import bot

from datetime import datetime
from random import randint
from sql import getIds, insertUser, alterUserById, deleteById

def browhat_message(): 
    browhat = ("Well, you should greet me first!", "What?", "Didnt your mom give you basic education?")
    
    return browhat[0]

@bot.command()
async def config(ctx, *args):
    new_entries = getIds()
    sampleArgs = ('name', 'zodiac', 'birthday', 'timezone')
    sampleZodiacs = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces']
    userId = ctx.author.id
    setting = args[0].lower()
    value = args[1].lower()
    
    if userId not in new_entries:
        insertUser(userId)
    
    if setting not in sampleArgs:
        return await ctx.message.channel.send("Invalid setting")
    elif setting == "zodiac" and value not in sampleZodiacs:
        return await ctx.message.channel.send(f"{value.capitalize()} is not a valid zodiac.")
    else:
        alterUserById(userId, setting, value)
        return await ctx.message.channel.send(f"{setting.capitalize()} successfully set.")
        
@bot.command()
async def delete(ctx, *args):
    userId = ctx.author.id
    deleteById(userId)
    return await ctx.message.channel.send("User deleted successfully.")
    
    

