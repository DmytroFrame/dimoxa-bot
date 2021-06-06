import discord
from discord.ext import commands
from pymongo import cursor

import models.functions as func


class IdiotCommands(commands.Cog):
    """
        
    """
    def __init__(self, client):
        self.client = client
    

    @commands.command()
    async def aboba(self, ctx):
        await ctx.send("ты гей")





def setup(client):
    client.add_cog(IdiotCommands(client))






