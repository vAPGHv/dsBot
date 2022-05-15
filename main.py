# -------=imports=-------
import discord
import requests as req
from bs4 import BeautifulSoup as BS
from settings import *
import random


class MyClient(discord.Client):
    async def on_message(self, message):
        lowerm = message.content.lower()

        for m in cens:
            if m in lowerm:
                await message.delete()

        if '/img' in lowerm:
            reg = message.content.split("/img ")[1]  # get the word after the command
            url = f"https://www.google.com/search?q={reg}&client=opera&hs=nkI&hl=ru&sxsrf=APq-WBuUWCpyLYYduHWl9vqF9dG_IIvdpg:1649445742756&source=lnms&tbm=isch&sa=X&ved=2ahUKEwizzsqcmIX3AhVM-yoKHcKBCg0Q_AUoAXoECAEQAw&biw=2519&bih=1299&dpr=1"

            r = req.get(url)

            soup = BS(r.content, "html.parser")
            list1 = []

            for i in soup.select("img", class_="Q4LuWd"):
                list1.append(i.get("src"))

            randel = list1[random.randrange(1, len(list1))]
            randel = req.get(randel).content

            with open(f"123.jpg", "wb") as file:
                file.write(randel)

            await message.reply(file=discord.File('123.jpg'))


client = MyClient()
client.run(TOKEN)
