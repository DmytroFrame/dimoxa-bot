# -- coding: utf-8 --
import discord
from discord.ext import commands
from pymongo import MongoClient

from models.functions import getSettings, passwordGen, setStatus, getStatus, delStatus
from models.mcrcon import sendCommand
from models.snowflakes import checkBotTime

# from actions.register import register
# from actions.addperson import addperson



clientDB = MongoClient(getSettings("mongoData")["url"])
db = clientDB[getSettings("mongoData")["database"]]
collection = db[getSettings("mongoData")["collection"]]

client = commands.Bot(
    command_prefix = getSettings("discordData")["prefix"])



@client.event
async def on_ready():
    # await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="на лисицу"))
    # await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="лісову пісню"))
    print("I'm Online")


# @client.command( pass_context = True)
# @commands.has_permissions(administrator = True)
# async def addperson(ctx, user:discord.Member, times):
#     if collection.count_documents({"_id": str(user.id)}):
#         timeMess = ""
#         if times[-1:].lower() == "m":
#             timeMess = f"на **{times[:-1]} месяц**"
#             times = str(int(times[:-1]) * 31) + "d"

#         elif times[-1:].lower() == "i":
#             timeMess = "**Навсегда**"
#             times = "5y"

#         elif times[-1:].lower() == "s":
#             timeMess = f"на **{times[:-1]} секунд**"

#         elif times[-1:].lower() == "h":
#             timeMess = f"на **{times[:-1]} часов**"
        
#         elif times[-1:].lower() == "d":
#             timeMess = f"на **{times[:-1]} дней**"
        
#         else:
#             times = "хуйня"
        

#         if times != "хуйня":
#             for i in collection.find({"_id": str(user.id)}):
#                 await ctx.send(f'Выдан игроку **{i["nickName"]}** проходка {timeMess}.')
#                 await user.send(f"Вам дали проходку {timeMess}.\nIP: play.mcteaparty.fun\n#СпасибоТебе!")
#                 role = discord.utils.get(user.guild.roles, id=821119675324170250)
#                 await user.add_roles(role)
#                 sendCommand([f'wh add {i["nickName"]} {times}'])
#         else:
#             await ctx.send("Братик, ты хуйню написал, я это делать не буду!")
#     else:
#         await ctx.send(f"Игрока **<@{user.id}>** нет в базе")









@client.command(pass_context = True)
async def reg(ctx):
    if checkBotTime(ctx.author.id):
        try:
            user = db["users"].find_one({"discordID": str(ctx.author.id)})
        except:
            user = None

        if user is None:
            await ctx.author.send(f"Привет {ctx.message.author.mention}!\nЯ знаю как попасть на сервер.\nНапиши мене ник который ты хочеш, через команду **!regnik** *Ник*")
            setStatus(ctx.author.id, "addnik")

        else:
            await ctx.send(f"Я тебя занаю, ты {user['username']}")
    else:
        await ctx.send("Я не отвечаю молокососом!")


@client.command(pass_context = True)
async def regnik(ctx, username):
    if getStatus(ctx.author.id) == "addnik":
        if db["users"].count_documents({"username": username}):
            await ctx.author.send(f"Привет {ctx.message.author.mention}\n{username}")
            setStatus(ctx.author.id, f"addpass:{username}")

        else:
            await ctx.send("Сорян, уже есть такой поц")


    



# @client.command( pass_context = True)
# async def regtwink(ctx):
#     for i in collection.find({"_id": str(ctx.author.id)}):
#         if i["twinkUsed"] == False:
#             await ctx.send("Оки-доки")

#             password = passwordGen()
            
#             collection.update_one({"_id": str(ctx.author.id)}, {"$set": {"twinkUsed": True }})

#             await ctx.author.send(f'Твой временный пароль: ||{password}|| для **{i["nickName"]}T**\nЧтобы изменить пароль напиши команду на сервере /changepassword временный-пароль новый-пароль.')

#             sendCommand([f'whitelist add {i["nickName"]}T', f'authme register {i["nickName"]}T {password}', f'team join TwinkNew {i["nickName"]}T'])
        
#         else:await ctx.send("У тебя уже есть твинк аккаунт!")


@client.command( pass_context = True)
async def resetpass(ctx):
    nickName = collection.find_one({"_id": str(ctx.author.id)})["nickName"]

    password = passwordGen()

    await ctx.send("Брат, без проблем.")
    await ctx.author.send(f'Твой временный пароль: ||{password}|| для **{nickName}**\nЧтобы изменить пароль напиши команду на сервере /changepassword временный-пароль новый-пароль.')

    sendCommand([f'authme changepassword {nickName} {password}'])



# @client.command( pass_context = True)
# async def resetpasstwink(ctx):
#     nickName = collection.find_one({"_id": str(ctx.author.id)})["nickName"]

#     password = passwordGen()

#     await ctx.send("Брат, без проблем.")
#     await ctx.author.send(f'Твой временный пароль: ||{password}|| для **{nickName}Twink**\nЧтобы изменить пароль напиши команду на сервере /changepassword временный-пароль новый-пароль.')

#     sendCommand([f'authme changepassword {nickName}Twink {password}', f'authme changepassword {nickName}T {password}'])


@client.command( pass_context = True)
@commands.has_permissions(administrator = True)
async def delete(ctx, arg):
    for i in collection.find({"_id": arg[3:-1]}):
        collection.delete_one({"_id": arg[3:-1]})
        
        sendCommand([f'whitelist remove {i["nickName"]}', f'authme unregister {i["nickName"]}'])

        await ctx.send(f'Удалил <@{arg[3:-1]}>')


@client.command( pass_context = True)
@commands.has_role(802536798760206406)
async def broadcast(ctx, *, content):
    sendCommand([f'broadcast {content}'])
    await ctx.send("Ваши слова были услышаны на сервере")


@client.command( pass_context = True)
@commands.has_role(802536798760206406)
async def ban(ctx, user:discord.Member, times, *, content):
    if collection.count_documents({"_id": str(user.id)}):
        typeTime = ""
        if times[-1:] == "d" or times[-1:] == "D":typeTime = "дней"
        elif times[-1:] == "h" or times[-1:] == "H":typeTime = "часа"

        for i in collection.find({"_id": str(user.id)}):
            await ctx.send(f'Игрок **{i["nickName"]}** был забанен')
            await user.send(f"Тебя забанил <@{ctx.author.id}> на {times[:-1]} {typeTime}.\nПричина: **{content}**")

            sendCommand([f'tempban {i["nickName"]} {times} {content}'])

    else:await ctx.send(f"Игрока **<@{user.id}>** нет в базе")

@client.command( pass_context = True)
@commands.has_role(802536798760206406)
async def pardon(ctx, user:discord.Member):
    if collection.count_documents({"_id": str(user.id)}):
        for i in collection.find({"_id": str(user.id)}):
            await ctx.send(f'Игрок **{i["nickName"]}** был разбанин')
            await user.send(f"Тебя розбанил <@{ctx.author.id}>")

            sendCommand([f'pardon {i["nickName"]}'])

    else:await ctx.send(f"Игрока **<@{user.id}>** нет в базе")

@client.command(pass_context = True)
@commands.has_role(802536798760206406)
async def kick(ctx, user:discord.Member, *, content):
    if collection.count_documents({"_id": str(user.id)}):
        for i in collection.find({"_id": str(user.id)}):
            await ctx.send(f'Игрок **{i["nickName"]}** был кикнут')
            await user.send(f"Тебя кикнул <@{ctx.author.id}>\nПричина: **{content}**")

            sendCommand([f'kick {i["nickName"]} {content}'])

    else:await ctx.send(f"Игрока **<@{user.id}>** нет в базе")


@client.command(pass_context = True)
@commands.has_role(802536798760206406)
async def mute(ctx, user:discord.Member):
    if collection.count_documents({"_id": str(user.id)}):
        for i in collection.find({"_id": str(user.id)}):
            await ctx.send(f'Игрок **{i["nickName"]}** был замучен')
            await user.send(f"Тебя замутил <@{ctx.author.id}>")

            sendCommand([f'mute {i["nickName"]}'])

    else:await ctx.send(f"Игрока **<@{user.id}>** нет в базе")


@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def addfbi(ctx, user:discord.Member):
    if collection.count_documents({"_id": str(user.id)}):
        for i in collection.find({"_id": str(user.id)}):
            await ctx.send(f'Игрок **{i["nickName"]}** назначен в отряд **FBI**')
            await user.send(f"Глава FBI **<@{ctx.author.id}>** назначил вас на службу в **FBI**\n\n**Команды для криминалистики**\n**#Режим проверки**\nЧтобы включить режим проверки, введите команду /co i. Кликните ЛКМ по блоку, чтобы узнать, какие блоки на этом месте были поставлены или сломаны. Показывается также время изменения блоков и никнеймы игроков (или имена сущностей), которые эти блоки изменили. Вся информация выводится в чат. Кликните ПКМ по грани блока, чтобы узнать историю изменений блока, который находился по другую сторону от грани. Нажмите ПКМ по любому механизму (кнопке, рычагу, двери), чтобы узнать, кто и когда использовал его. Режим проверки отключается повторным вводом команды /co i.\n\n**#Просмотр логов**\nПосмотреть все сообщения, отправленные игроком Notch за последние 15 минут./co lookup u:Notch a:chat t:15m\nПосмотреть все входы игрока Notch на сервер./co lookup u:Notch a:login\n**#Другие параметры**\nblock — блок поставлен/сломан \n+block — блок поставлен \n-block — блок сломан \nclick — взаимодействие игрока с блоком \ncontainer — предмет взят или положен в контейнер \n+container — предмет положен в контейнер \n-container — предмет взят из контейнера \nkill — убит моб или другая энтити \nchat — отправлено сообщение в чат \ncommand — команда выполнена \nsession — вход или выход игрока с сервера \n+session — вход игрока на сервер \n-session — выход игрока с сервера \nusername — изменён никнейм")
            
            role = discord.utils.get(user.guild.roles, id=834474315922931733)
            await user.add_roles(role)

            sendCommand([f'pex user {i["nickName"]} group set FBI', f'team join FBI {i["nickName"]}'])

    else:await ctx.send(f"Игрока **<@{user.id}>** нет в базе")



@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def unfbi(ctx, user:discord.Member):
    if collection.count_documents({"_id": str(user.id)}):
        for i in collection.find({"_id": str(user.id)}):
            await ctx.send(f'Игрок **{i["nickName"]}** отстранен от службы **FBI**')
            await user.send(f"Глава FBI **<@{ctx.author.id}>** уволил вас из **FBI**")

            role = discord.utils.get(user.guild.roles, id=834474315922931733)
            await user.remove_roles(role)

            sendCommand([f'pex user {i["nickName"]} group remove FBI', f'team leave {i["nickName"]}'])

    else:await ctx.send(f"Игрока **<@{user.id}>** нет в базе")
    

@client.command( pass_context = True)
@commands.has_permissions(administrator = True)
async def adminreg(ctx, amount = 30):
    nickName = collection.find_one({"_id": str(ctx.author.id)})["nickName"]
    sendCommand([f'op {nickName}', f'deop {nickName}'], amount)

    await ctx.send(f'Окей, дал тебе админку на {amount} секунд')





@client.command( pass_context = True)
@commands.has_permissions(administrator = True)
async def dayadmin(ctx, amount = 30):
    nickName = collection.find_one({"_id": str(ctx.author.id)})["nickName"]
    sendCommand([f'op {nickName}', f'deop {nickName}'], amount)

    await ctx.send(f'Окей, дал тебе админку на {amount} секунд')



@client.command( pass_context = True)
async def player(ctx, arg):
    twinkUsed = ""
    if collection.count_documents({"nickName": arg}):
        for i in collection.find({"nickName": arg}):
            await ctx.send(f'Это <@{ i["_id"] }> \nБаланс: **{ i["money"] }**¥')

    elif collection.count_documents({"_id": arg[3:-1]}):
        for i in collection.find({"_id": arg[3:-1]}):
            await ctx.send(f'Это { i["nickName"] } \nБаланс: **{ i["money"] }**¥')

    else:await ctx.send(f"Товарища **{arg}** у нас нету и не было!")


@client.command( pass_context = True )
@commands.has_permissions(administrator = True)
async def echo(ctx, *, content):
    await ctx.channel.purge( limit = 1)
    await ctx.send(content)




# @client.command( pass_context = True)
# async def reglist(ctx):
#     await ctx.send("Зарегистрировано", collection.count(), "игроков")


# @client.command( pass_context = True)
# async def clear(ctx, amount = 6):
#     await ctx.channel.purge( limit = amount))



# @client.event
# async def on_message(message):
#     if message.content.lower() == "дай админку":
#         rcon = upSession()
#         respons = rcon.send('op DmytroFrame')
#         rcon.disconnect()
#         await message.channel.send("Окей, держы")








client.run(getSettings("discordData")["token"])

