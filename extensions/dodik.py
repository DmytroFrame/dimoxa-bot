import discord
from discord.ext import commands




def setup(client):


    # @commands.Cog.listener()
    # async def on_ready(self):
    #     await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="на лисицу"))
    #     print("good")


    @client.command( pass_context = True)
    async def hi(ctx):
        await ctx.send("hi debil2.0 for reload")



