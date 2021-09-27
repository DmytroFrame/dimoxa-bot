import asyncio
import discord
from discord.ext import commands
from pymongo import cursor
from random import randint

import models.functions as func
from models.coolDown import coolDown

class IdiotCommands(commands.Cog):
    """
        
    """
    def __init__(self, client):
        self.client = client
    

    @commands.command()
    async def aboba(self, ctx):
        await ctx.send("ты гей")


    @commands.command()
    async def dick(self, ctx):
        if coolDown(ctx.author.id, 300):
            return await ctx.send("Не наглей")            

        size = str(randint(4, 17))
        if randint(1, 20) > 3:
            await ctx.send(f"Размер твоего члена {size} см")
        else:
            await ctx.send("У тебя нету члена")
            await asyncio.sleep(1)
            await ctx.send(f"у тебя дырка (вагина) глубеной {size} см")






def setup(client):
    client.add_cog(IdiotCommands(client))






