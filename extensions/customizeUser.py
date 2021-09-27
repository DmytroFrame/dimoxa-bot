import os
import discord
from discord.ext import commands
# from discord_components import Button, ButtonStyle

import models.functions as func
from models.async_mcrcon import MinecraftClient

class CustomizeUser(commands.Cog):
    """
        Customize user
    """
    def __init__(self, client):
        self.client = client


    @commands.command(aliases=['editpass'])
    async def editpassword(self, ctx, password):
        """
            editpass - изменить пароль
        """
        if not func.check_validation_password(password):
            await ctx.send("хуйня")
        else:
            await ctx.send("Пароль я поменял")
            cursor = func.cursor_database('users')
            fullUserData = cursor.find_one({"discordID": ctx.author.id})
            cursor.update_one({"_id": fullUserData['_id']}, {"$set": {"password": password}})

            rconData = func.getSettings('rconData')
            async with MinecraftClient(rconData['address'], rconData['port'], rconData['password']) as mc:
                await mc.send(f"authme changepassword {fullUserData['username']} {password}")

            await ctx.send(str("успешно"))


    @commands.command(aliases=['onip'])
    async def onfixetip(self, ctx):
        await ctx.send("я включил тебе двойную аутентификацию")
        cursor = func.cursor_database('users')
        cursor.update_one({"discordID": ctx.author.id}, {"$set": {"fixedIP": True}})


    @commands.command(aliases=['offip'])
    async def offfixetip(self, ctx):
        await ctx.send("я выключил тебе двойную аутентификацию")
        cursor = func.cursor_database('users')
        cursor.update_one({"discordID": ctx.author.id}, {"$set": {"fixedIP": False}})


    @commands.command(aliases=['resetip'])
    async def resetfixetip(self, ctx):
        await ctx.send("я сбросил твой апий адрес")
        cursor = func.cursor_database('users')
        cursor.update_one({"discordID": ctx.author.id}, {"$set": {"lastIP": None}})
        
        



    




def setup(client):
    client.add_cog(CustomizeUser(client))
    