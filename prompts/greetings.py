import time
from datetime import datetime
import pytz
from requests import get_Horoscope
from sql import getIds, fetchById
from reminderSql import getRemindersDates


async def setup(orig_msg):
    # send instructions
    return await orig_msg.channel.send("### Hey!\nIs this the first time I see you here? \nYou should run those commands: \nFirst, setup your name with: .config name [Name]\n Then, setup your birthday: .config birthday [xxxx-xx-xx] \n And then your zodiac sign with: .config zodiac [sign]")
    
async def greetings(message):
    await message.channel.typing()
    
    userId = message.author.id
    users = getIds()
    user = fetchById(userId)
    remindersDates = getRemindersDates(userId)
    
    if userId not in users:
        return await setup(message)

    name = user[0][4]
    zodiac = user[0][2]
    
    secondssince = int(time.time())
    
    horoscope = await get_Horoscope(zodiac.lower())
    
    birthdaywhen = user[0][1]
    
    date = f'<t:{secondssince}:F>'
    birthday = f'<t:{birthday_When(birthdaywhen)}:R>'
    if datetime.now().date() in remindersDates:
        await message.channel.send("You have a reminder set for today.")
 
    await message.channel.send(f'### Hi {name}, {greetingHour()}:sparkles: \n:date: Today is {date}! \n\n:crystal_ball: The horoscope for **{zodiac}** :{zodiac.lower()}: today is: \n*{horoscope}* \n\n:fireworks: **Your birthday** is {birthday}.\n')


#I despise this.
def birthday_When(birthdaydt):
    nowdt = datetime.now()
    
    # if the month of birth is bigger than the actual month
    if birthdaydt.month > nowdt.month:
        return int(datetime(nowdt.year, birthdaydt.month, birthdaydt.day).timestamp())
    
    return int(datetime(nowdt.year + 1, birthdaydt.month, birthdaydt.day).timestamp())

def greetingHour():
    greeting = ('good morning! :city_sunset:', 'good afternoon! :cityscape:', 'good evening! :night_with_stars:', 'good night! :milky_way:')
    hour = datetime.now().hour
    if hour >= 6 and hour < 12:
        return greeting[0]
    if hour >= 12 and hour < 18:
        return greeting[1]
    if hour >= 18 and hour <= 23:
        return greeting[2]
    if hour >= 0 and hour < 6:
        return greeting[3]

    
