import discord
from discord.ext import commands

description='sup'

intents = discord.Intents.default()
intents.message_content = True



bot = commands.Bot(command_prefix = '.', description = description, intents = intents)