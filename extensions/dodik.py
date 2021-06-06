import discord
from discord.ext import commands




def setup(client):


    # @commands.Cog.listener()
    # async def on_ready(self):
    #     await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="на лисицу"))
    #     print("good")


    @commands.command()
    async def his(self, ctx):
        await ctx.send("hi debil2.0 for reload")



