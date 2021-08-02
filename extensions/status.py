import discord
from discord.ext import commands
# from discord_components import DiscordComponents

class Status(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you mom"))
        # DiscordComponents(self.client)
        print("\n✅ Bot his online")

    





def setup(client):
    client.add_cog(Status(client))