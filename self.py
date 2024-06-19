import discord
import os
import asyncio
import random
import io
import aiohttp
import ctypes
import requests
import datetime
from discord.ext import commands
from discord.utils import get         
from discord.ext.commands import bot

prefix = "."

token = "TOKEN"

if os.name == "console":
      ctypes.windll.caducrs.SetConsoleTitleW("Self Bot")
client = commands.Bot(command_prefix = prefix, self_bot=True)
client.remove_command('help')
ascii = f"""

Self Bot - oN 

By: caducrs


"""
print(ascii)


#comando para dar clear em privados
@client.command()
async def purge(ctx, limit: int=None):
    async for message in ctx.message.channel.history(limit=None).filter(lambda m: m.author == client.user):
            try:
                await message.delete()
            except:
                pass 




#automação de banimento pelo bot Rony discord
@client.command()
async def ronyban(ctx):
    await ctx.message.delete()
    for member in list(ctx.guild.members):
        message = await ctx.send("n!ban " + member.mention)
        await message.delete()
        await asyncio.sleep(0.5)



#puxa o seu avatar
@client.command()
async def av(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    format = "gif"
    user = user or ctx.author
    if user.is_avatar_animated() != True:
        format = "png"
    avatar = user.avatar_url_as(format=format if format != "gif" else None)
    async with aiohttp.ClientSession() as session:
        async with session.get(str(avatar)) as resp:
            image = await resp.read()
    with io.BytesIO(image) as file:
        await ctx.send(file=discord.File(file, f"Avatar.{format}"))






#iniciando o selfbot e definindo que o bot não é um bot normal.
client.run(token, bot=False)