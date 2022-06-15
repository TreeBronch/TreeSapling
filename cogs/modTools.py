from collections import UserList
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions



class modTools(commands.cog, name='Mod Commands'):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='ban')
    @has_permissions(ban_members=True)
    def ban(self, ctx, user, reason):
        b=False
        for mem in discord.Guild.members:
            if user == mem:
                b=True
                break
        if b:
            try:
                discord.Member.ban(user)
                if reason!=None:
                    user.send("Ya got banned cuz this nerd said this")
            except:
                ctx.send("Somethin sus happened and I cant do it")
            pass
        else:
            ctx.send("User {user} is not in this server smh")