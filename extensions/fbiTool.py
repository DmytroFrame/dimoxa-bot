import os
import discord
from discord.ext import commands
# from discord_components import Button, ButtonStyle

import models.functions as func



def setup(client):
    pass


    # @client.command(pass_context = True)
    # @commands.has_permissions(administrator = True)
    # async def addfbi(ctx, user:discord.Member):
    # if collection.count_documents({"_id": str(user.id)}):
    #     for i in collection.find({"_id": str(user.id)}):
    #         await ctx.send(f'Игрок **{i["nickName"]}** назначен в отряд **FBI**')
    #         await user.send(f"Глава FBI **<@{ctx.author.id}>** назначил вас на службу в **FBI**\n\n**Команды для криминалистики**\n**#Режим проверки**\nЧтобы включить режим проверки, введите команду /co i. Кликните ЛКМ по блоку, чтобы узнать, какие блоки на этом месте были поставлены или сломаны. Показывается также время изменения блоков и никнеймы игроков (или имена сущностей), которые эти блоки изменили. Вся информация выводится в чат. Кликните ПКМ по грани блока, чтобы узнать историю изменений блока, который находился по другую сторону от грани. Нажмите ПКМ по любому механизму (кнопке, рычагу, двери), чтобы узнать, кто и когда использовал его. Режим проверки отключается повторным вводом команды /co i.\n\n**#Просмотр логов**\nПосмотреть все сообщения, отправленные игроком Notch за последние 15 минут./co lookup u:Notch a:chat t:15m\nПосмотреть все входы игрока Notch на сервер./co lookup u:Notch a:login\n**#Другие параметры**\nblock — блок поставлен/сломан \n+block — блок поставлен \n-block — блок сломан \nclick — взаимодействие игрока с блоком \ncontainer — предмет взят или положен в контейнер \n+container — предмет положен в контейнер \n-container — предмет взят из контейнера \nkill — убит моб или другая энтити \nchat — отправлено сообщение в чат \ncommand — команда выполнена \nsession — вход или выход игрока с сервера \n+session — вход игрока на сервер \n-session — выход игрока с сервера \nusername — изменён никнейм")
            
    #         role = discord.utils.get(user.guild.roles, id=834474315922931733)
    #         await user.add_roles(role)

    #         sendCommand([f'pex user {i["nickName"]} group set FBI', f'team join FBI {i["nickName"]}'])

    # else:await ctx.send(f"Игрока **<@{user.id}>** нет в базе")



    # @client.command(pass_context = True)
    # @commands.has_permissions(administrator = True)
    # async def unfbi(ctx, user:discord.Member):
    # if collection.count_documents({"_id": str(user.id)}):
    #     for i in collection.find({"_id": str(user.id)}):
    #         await ctx.send(f'Игрок **{i["nickName"]}** отстранен от службы **FBI**')
    #         await user.send(f"Глава FBI **<@{ctx.author.id}>** уволил вас из **FBI**")

    #         role = discord.utils.get(user.guild.roles, id=834474315922931733)
    #         await user.remove_roles(role)

    #         sendCommand([f'pex user {i["nickName"]} group remove FBI', f'team leave {i["nickName"]}'])

    # else:await ctx.send(f"Игрока **<@{user.id}>** нет в базе")


    # @commands.command(aliases=['editpass'])
    # async def editpassword(self, ctx, password):
    #     if not func.check_validation_password(password):
    #         await ctx.send("хуйня")
    #     else:
    #         await ctx.send("пароль я поменял")
    #         cursor = func.cursor_database('users')
    #         cursor.update_one({"discordID": ctx.author.id}, {"$set": {"password": password}})
    #         await ctx.send(str("good"))

    