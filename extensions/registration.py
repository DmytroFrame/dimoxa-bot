from models.mcrcon import command
import discord
from discord.ext import commands



import models.functions as func
import models.cashTool as casht


class Registration(commands.Cog):
    """
        registation users
    """
    def __init__(self, client):
        self.client = client

    @commands.has_role(func.getSettings('roles_id')['logged_no'])
    @commands.command()
    async def reg(self, ctx, username):
        """
            каво?
        """
        if not self.check_validation(username):
            await ctx.send("С таким ноком можеш не заходить!")
        
        else:
            if self.check_username_on_db(username):
                await ctx.send("Даный ник нейм уже занят")

            else:
                password = func.passwordGen(12)

                await ctx.author.send(f"окей поздровляю тебя твой ||{password}||")
                
                member = ctx.message.author
                
                role = discord.utils.get(member.guild.roles, id=func.getSettings('roles_id')['logged_yes'])
                await member.add_roles(role)

                role = discord.utils.get(member.guild.roles, id=func.getSettings('roles_id')['logged_no'])
                await member.remove_roles(role)

                self.registration_on_db(username, password, ctx.author.id)

    # @commands.command(pass_context=True)
    # async def addpass(self, ctx, password = None):
    #     status = casht.getStatus(ctx.author.id)
    #     if status[0] == "wait_password":
    #         if password is None:
    #             password = func.passwordGen(12)

    #         if not self.check_validation_password(password):
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


    def check_validation(self, userString):
        if len(userString) < 3 or len(userString) > 22:
            return False
         
        validChars = "_-qwertyuiopasdfghjklzxcvbnm0123456789QWERTYUIOPASDFGHJKLZXCVBNM"
        customString = ""
        for user in userString:
            for valid in validChars:
                if user == valid:
                    customString += valid
                    break

        return userString == customString


    def check_validation_password(self, password):
        if len(password) < 8 or len(password) > 32:
            return False
         
        validChars = "_-qwertyuiopasdfghjklzxcvbnm0123456789QWERTYUIOPASDFGHJKLZXCVBNM@#$%!"
        customString = ""
        for user in password:
            for valid in validChars:
                if user == valid:
                    customString += valid
                    break

        return password == customString


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






