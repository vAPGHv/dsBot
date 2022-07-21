# -------=imports=-------
import discord
import requests as req
from bs4 import BeautifulSoup as BS
from settings import *
import random
from getimg import getimg


class MyClient(discord.Client):
    async def on_message(self, message):
        try:
            lowerm = message.content.lower()

            for m in cens:
                if m in lowerm:
                    await message.delete()

            if '/img' in lowerm[0:4]:
                reg = message.content.split("/img ", maxsplit=1)[1]  # get the word after the command
                print(reg)
                getimg(reg)

                await message.reply(file=discord.File('img.jpg'))
        except Exception as ex:
            await message.reply(ex)
            print(ex)
            return ex


client = MyClient()
client.run(TOKEN)
