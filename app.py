import os
import discord
from discord.ext import commands

import models.functions as func


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
    async def reload(ctx, extension = None):
        if extension == None:
            for filename in os.listdir("./extensions"):
                if filename.endswith(".py"):
                    try:
                        client.unload_extension(f"extensions.{filename[:-3]}")
                    finally:
                        try:
                            message = load_model(filename[:-3])
                            await ctx.send(message)
                            print(message)
                        except:
                            pass

        else:
            try:
                client.unload_extension(f"extensions.{extension}")
            finally:
                message = load_model(extension)
                await ctx.send(message)
                print(message)



if __name__ == "__main__":
    discordData = func.getSettings("discordData")
    client = commands.Bot(command_prefix = discordData["prefix"])
    main(client)
    client.run(discordData["token"])