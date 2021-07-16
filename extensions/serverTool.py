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


    @commands.command(name = 'player')
    @commands.has_role(func.getSettings('roles_id')['logged_yes'])
    async def get_player_info(self, ctx, user):
        def get_id(user: str) -> int:
            try:
                user = user.split('!')
                user = user[1].split('>')
                return int(user[0])
            except:
                return 0


        cursor = func.cursor_database('users')
        if cursor.count_documents({"username": user}):
            for data in cursor.find({"username": user}):
                await ctx.send(f'Это <@{data["discordID"]}>')#Баланс: **{ i["money"] }**¥

        elif cursor.count_documents({"discordID": get_id(user)}):
            for data in cursor.find({"discordID": get_id(user)}):
                await ctx.send(f'Это **{data["username"]}**')#Баланс: **{ i["money"] }**¥

        else:
            await ctx.send(f"Товарища **{user}** у нас нету и не было!")



def setup(client):
    client.add_cog(ServerTool(client))