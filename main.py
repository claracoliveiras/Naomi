from discord import ChannelType
from dotenv import load_dotenv
from prompts import greetings
from botinit import bot
import os
import logging
from commands import profilesetup
from users import db

load_dotenv()
 
db.entries = db.read_db()
 
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

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

    

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
bot.run(os.getenv('TOKEN'), log_handler=handler)
