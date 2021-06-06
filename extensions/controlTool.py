import discord
from discord.ext import commands

import models.functions as func 
from models.async_mcrcon import MinecraftClient



def setup(client):

    @client.command(pass_context = True)
    @commands.has_role(func.getSettings('roles_id')['controlpanel'])
    async def broadcast(ctx, *, content):
        rconData = func.getSettings('rconData')
        async with MinecraftClient(rconData['address'], rconData['port'], rconData['password']) as mc:
            await mc.send(f'broadcast {content}')

        await ctx.send("Ваши слова были услышаны на сервере")



    @client.command( pass_context = True )
    @commands.has_role(func.getSettings('roles_id')['controlpanel'])
    async def echo(ctx, *, content):
        await ctx.channel.purge( limit = 1)
        await ctx.send(content)


    # @client.command( pass_context = True)
    # @commands.has_role(802536798760206406)
    # async def ban(ctx, user:discord.Member, times, *, content):
    #     if collection.count_documents({"_id": str(user.id)}):
    #         typeTime = ""
    #         if times[-1:] == "d" or times[-1:] == "D":typeTime = "дней"
    #         elif times[-1:] == "h" or times[-1:] == "H":typeTime = "часа"

    #         for i in collection.find({"_id": str(user.id)}):
    #             await ctx.send(f'Игрок **{i["nickName"]}** был забанен')
    #             await user.send(f"Тебя забанил <@{ctx.author.id}> на {times[:-1]} {typeTime}.\nПричина: **{content}**")

    #             sendCommand([f'tempban {i["nickName"]} {times} {content}'])

    #     else:await ctx.send(f"Игрока **<@{user.id}>** нет в базе")


    # @client.command( pass_context = True)
    # @commands.has_role(802536798760206406)
    # async def pardon(ctx, user:discord.Member):
    #     if collection.count_documents({"_id": str(user.id)}):
    #         for i in collection.find({"_id": str(user.id)}):
    #             await ctx.send(f'Игрок **{i["nickName"]}** был разбанин')
    #             await user.send(f"Тебя розбанил <@{ctx.author.id}>")

    #             sendCommand([f'pardon {i["nickName"]}'])

    #     else:await ctx.send(f"Игрока **<@{user.id}>** нет в базе")


    # @client.command(pass_context = True)
    # @commands.has_role(802536798760206406)
    # async def kick(ctx, user:discord.Member, *, content):
    #     if collection.count_documents({"_id": str(user.id)}):
    #         for i in collection.find({"_id": str(user.id)}):
    #             await ctx.send(f'Игрок **{i["nickName"]}** был кикнут')
    #             await user.send(f"Тебя кикнул <@{ctx.author.id}>\nПричина: **{content}**")

    #             sendCommand([f'kick {i["nickName"]} {content}'])

    #     else:await ctx.send(f"Игрока **<@{user.id}>** нет в базе")


    # @client.command(pass_context = True)
    # @commands.has_role(802536798760206406)
    # async def mute(ctx, user:discord.Member):
    #     if collection.count_documents({"_id": str(user.id)}):
    #         for i in collection.find({"_id": str(user.id)}):
    #             await ctx.send(f'Игрок **{i["nickName"]}** был замучен')
    #             await user.send(f"Тебя замутил <@{ctx.author.id}>")

    #             sendCommand([f'mute {i["nickName"]}'])

    #     else:await ctx.send(f"Игрока **<@{user.id}>** нет в базе")


