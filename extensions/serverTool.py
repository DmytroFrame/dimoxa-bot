import discord
from discord.ext import commands

import models.functions as func
from models.async_mcrcon import MinecraftClient


class ServerTool(commands.Cog):
    """
        ServerTool
    """
    def __init__(self, client):
        self.client = client

    
    @commands.command(pass_context=True)
    async def online(self, ctx):
        """
            !online - узнать количество игроков и кто на сервере
        """
        rconData = func.getSettings('rconData')
        async with MinecraftClient(rconData['address'], rconData['port'], rconData['password']) as mc:
            response = await mc.send('list')
        
        lastPlayers = int(response.split(' ')[2])
        maxPlayers = int(response.split(' ')[7])
        arrayPlayers = response.split(': ')[1].split(', ')

        if lastPlayers == 0:
            message = "На сервере сейчас никого нету"
            
        elif lastPlayers == 1:
            message = "На сервере сейчас только **{}**".format(arrayPlayers[0])
            
        elif lastPlayers > 1:
            message = "На сервере сейчас присутствует такие игроки как:"
            for player in arrayPlayers:
                message += f"\n  {player}"

            message += "\nСумарно **{}** игроков из **{}**".format(lastPlayers, maxPlayers)


        await ctx.send(message)


def setup(client):
    client.add_cog(ServerTool(client))