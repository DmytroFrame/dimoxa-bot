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
        self.minecraftCharArray = ['§0', '§1', '§2', '§3', '§4', '§5', '§6', '§7', '§8', '§9', '§a', '§b', '§c', '§d', '§e', '§f', '§k', '§l', '§m', '§n', '§o', '§r']
        self.__rcon = func.getSettings('rconData')
    
    def charFilter(self, string: str, charArray: list) -> str:
        for char in charArray:
            string = string.replace(char, '')
        return string

    @commands.command(pass_context=True)
    async def online(self, ctx):
        """
            !online - узнать количество игроков и кто на сервере
        """
        async with MinecraftClient(self.__rcon['address'], self.__rcon['port'], self.__rcon['password']) as mc:
            response = await mc.send('list')

        response = self.charFilter(response, self.minecraftCharArray + [',', '/'])

        lastPlayers = int(response.split()[1])
        maxPlayers = int(response.split()[3])
        if lastPlayers != 0:
            arrayPlayers = response.split(': ')[1].split()   

        if lastPlayers == 0:
            message = "На сервере сейчас никого нету"

        elif lastPlayers == 1:
            message = "На сервере сейчас только **{}**".format(arrayPlayers[0])

        elif lastPlayers > 1:
            message = "На сервере сейчас присутствует такие игроки как:"
            for player in arrayPlayers:
                message += f"\n   **`{player}`**"

            message += "\nСумарно **{}** игроков из **{}**".format(lastPlayers, maxPlayers)

        await ctx.send(message)

    @commands.command(aliases=['cmd'])
    @commands.has_permissions(administrator = True)
    async def command_to_server(self, ctx, *, cmd):
        """
            !cmd - отправить команду на сервер
        """
        async with MinecraftClient(self.__rcon['address'], self.__rcon['port'], self.__rcon['password']) as mc:
            response = await mc.send(cmd)

        response = self.charFilter(response, self.minecraftCharArray)
        await ctx.send(response)

    @commands.command(name='player')
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
                await ctx.send(f'Это <@{data["discordID"]}>')  # Баланс: **{ i["money"] }**¥

        elif cursor.count_documents({"discordID": get_id(user)}):
            for data in cursor.find({"discordID": get_id(user)}):
                await ctx.send(f'Это **{data["username"]}**')  # Баланс: **{ i["money"] }**¥

        else:
            await ctx.send(f"Товарища **{user}** у нас нету и не было!")


def setup(client):
    client.add_cog(ServerTool(client))
