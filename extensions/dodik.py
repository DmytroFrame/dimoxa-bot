import discord
from discord.ext import commands
from discord_components import button, ButtonStyle



def setup(client):
    # pass

    # @client.event
    # async def on_message(message):
    #     member = message.author
                
    #     role = discord.utils.get(member.guild.roles, id= 850964243939721246)
    #     await member.add_roles(role)


    # @client.command() # начало команды
    # # @client.has_permissions(administrator = True) # нужны права администратора? - да
    # async def ar(ctx, autoroles): #сама команда и что ей надо указать, это prefix, комаду и НАЗВАНИЕ роли.
    #     for guild in client.guilds: # оно ищет на сервере людей
    #         for member in guild.members: # и тут делается все работа для member-a
    #             autoroles2 = discord.utils.get(ctx.message.guild.roles, id = int(autoroles)) # нахождение айди по названию, иначе будет ошибка(у меня)
    #             await member.add_roles(autoroles2) # само добавление роли
    #     emb = discord.Embed(description = 'Роли успешно добавлены ВСЕМ участникам Discord сервера.')
    #     await ctx.send(embed = emb) # теперь бот сообщает что всё вышло.

    # @commands.command() # начало команды
    # @commands.has_permissions(administrator = True) # нужны права администратора? - да
    # async def ar(self, ctx, autoroles): #сама команда и что ей надо указать, это prefix, комаду и НАЗВАНИЕ роли.
    #     for guild in self.bot.guilds: # оно ищет на сервере людей
    #         for member in guild.members: # и тут делается все работа для member-a
    #             autoroles2 = discord.utils.get(ctx.message.guild.roles, name = autoroles) # нахождение айди по названию, иначе будет ошибка(у меня)
    #             await member.add_roles(autoroles2) # само добавление роли
    #     emb = discord.Embed(description = 'Роли успешно добавлены ВСЕМ участникам Discord сервера.')
    #     await ctx.send(embed = emb) # теперь бот сообщает что всё вышло.

    @client.command( pass_context = True)
    @commands.has_any_role(704366187567644702, 802536798760206406)
    async def hi(ctx):
        await ctx.send("hi debil2.0 for reload")



