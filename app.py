# -- coding: utf-8 --
import discord, os
from discord.ext import commands
from pymongo import MongoClient

from models.functions import getSettings, passwordGen, setStatus, getStatus, delStatus
from models.mcrcon import sendCommand
from models.snowflakes import checkBotTime



def main(client):
    def load_model(extension):
        try:
            client.load_extension(f"extensions.{extension}")
            return f"✅ Done load: {extension}"

        except Exception as error:
            return f"❌ Error load: {extension}\n 👆 Because: {error}"


    for filename in os.listdir("./extensions"):
        if filename.endswith(".py"):
            message = load_model(filename[:-3])
            print(message)


    @client.command()
    @commands.has_permissions(administrator = True)
    async def load(ctx, extension):
        message = load_model(extension)
        await ctx.send(message)
        print(message)


    @client.command()
    @commands.has_permissions(administrator = True)
    async def unload(ctx, extension):
        client.unload_extension(f"extensions.{extension}")
        message = f"❎ Unload model: {extension}"
        await ctx.send(message)
        print(message)


    @client.command()
    @commands.has_permissions(administrator = True)
    async def reload(ctx, extension):
        try:
            client.unload_extension(f"extensions.{extension}")
        finally:
            message = load_model(extension)
            await ctx.send(message)
            print(message)



if __name__ == "__main__":
    client = commands.Bot(command_prefix = getSettings("discordData")["prefix"])
    main(client)
    client.run(getSettings("discordData")["token"])