from discord import ChannelType
from dotenv import load_dotenv
from prompts import greetings
from botinit import bot
import os
import logging
from commands import profilesetup
from commands.reminders import dailyReminder
from users import db

load_dotenv()
 
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    print(db.new_entries)

@bot.event
async def on_message(message):
    print(f'{message.channel}: {message.author}: {message.author.name}: {message.content}')
    #temporary greeting samples
    greetingSamples = ('gm', 'good morning', 'good meowning')
    if message.channel.type != ChannelType.private:
        return
    if message.author == bot.user:
        return
    if message.content in greetingSamples:
        await greetings.greetings(message)
        
    await bot.process_commands(message)

    
bot.run(os.getenv('TOKEN'))
