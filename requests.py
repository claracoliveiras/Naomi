import aiohttp
import json

#its like that cause i only use horoscopes api now lol
async def get_Horoscope(sign):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily?sign={sign}&day=TODAY") as response:
            data = await response.text()
            data = json.loads(data)
            horoscope_data = data['data']['horoscope_data']
            return horoscope_data
