import discord
from discord.ext import commands

import models.functions as func
import models.cashTool as casht

from models.async_mcrcon import MinecraftClient


class Registration(commands.Cog):
    """
        registation users
    """
    def __init__(self, client):
        self.client = client

    
    @commands.command(name = 'reg')
    # @commands.has_role(func.getSettings('roles_id')['logged_no'])
    async def registration(self, ctx, username):
        """
            !reg ник - команда для рега
        """
        member = ctx.message.author
        roleYes = discord.utils.get(member.guild.roles, id=func.getSettings('roles_id')['logged_yes'])
        roleNo = discord.utils.get(member.guild.roles, id=func.getSettings('roles_id')['logged_no'])
        if not roleYes in member.roles and not roleNo in member.roles:
            role = discord.utils.get(member.guild.roles, id=func.getSettings('roles_id')['logged_no'])
            await member.add_roles(role)

        if not roleYes in member.roles:
            if not func.check_validation(username):
                await ctx.send("Придумай другой ник")
            
            else:
                if self.check_username_on_db(username):
                    await ctx.send("Данный никнейм уже занят")

                else:
                    password = func.passwordGen(12)

                    await ctx.send(f"Окей.. так и быть **{username}**")
                    await ctx.author.send(f"Поздравляю тебя **{username}**!\nТвой Пароль ||{password}||\nIP: play.mcteaparty.fun")#\nСкачать лаунчер можешь тут: https://cdn.discordapp.com/attachments/829879145253175366/852038720734625822/NightLauncher.exe\np.s. это бета)) 
                    
                    member = ctx.message.author
                    
                    role = discord.utils.get(member.guild.roles, id=func.getSettings('roles_id')['logged_yes'])
                    await member.add_roles(role)

                    role = discord.utils.get(member.guild.roles, id=func.getSettings('roles_id')['logged_no'])
                    await member.remove_roles(role)

                    self.registration_on_db(username, password, ctx.author.id)

                    rconData = func.getSettings('rconData')
                    async with MinecraftClient(rconData['address'], rconData['port'], rconData['password']) as mc:
                        await mc.send(f'authme register {username} {password}')


    # @commands.command(pass_context=True)
    # async def addpass(self, ctx, password = None):
    #     status = casht.getStatus(ctx.author.id)
    #     if status[0] == "wait_password":
    #         if password is None:
    #             password = func.passwordGen(12)

    #         if not func.check_validation_password(password):
    #             await ctx.send("херня пароль, придумай другой")

    #         else:
    #             await ctx.send("окей поздровляю тебя")
                
    #             member = ctx.message.author
    #             role = discord.utils.get(member.guild.roles, id=func.getSettings('roles_id')['logged_yes'])
    #             await member.add_roles(role)

    #             casht.delStatus(ctx.author.id)

    #             role = discord.utils.get(member.guild.roles, id=func.getSettings('roles_id')['logged_no'])
    #             await member.remove_roles(role)

    #             self.registration_on_db(status[1], password, ctx.author.id)
    
    
    def check_username_on_db(self, username):
        cursor = func.cursor_database('users')
        return cursor.count_documents({"username": username})


    def registration_on_db(self, username, password, discord_id):
        db = func.cursor_database()

        db["users"].insert_one({
            "username": username,
            "password": password,
            "email": None,
            "discordID": discord_id,
            "money": 0,
            "lastIP": None,
            "fixedIP": True
        })

        userID = db["users"].find_one({"username": username})["_id"]

        db["permissions"].insert_one({
            "_id": userID,
            "position": "player",
            "permission": "default"
        })

        db["bans"].insert_one({
            "_id": userID,
            "fullBan": False,
            "description": None,
            "banToData": None,
            "banUnixTime": None
        })



def setup(client):
    client.add_cog(Registration(client))






