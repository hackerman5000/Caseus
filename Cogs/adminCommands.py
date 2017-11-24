""" Contains admin only commands, c#clear, c#ping .etc... """
import discord
import inspect
import discord.ext.commands as commands
from discord.embeds import Embed
from HelperFunctions.EmbedGenerator import EmbGen
from time import sleep
import datetime


class AdminCommands:
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions()
    @commands.command(hidden=True)
    async def clear(self, ctx, number: int):
        """ Clears chat log 'n' messages."""
        await ctx.channel.purge(limit=number+1)

    @commands.has_permissions()
    @commands.command(hidden=True)
    async def ping(self, ctx):
        """ Tests self.bot Functionality """
        print("Pinged by..." + ctx.message.author.name)
        now = datetime.datetime.utcnow()
        delta = now - ctx.message.created_at
        re = f'Responded in {delta.microseconds} microseconds.'
        e = EmbGen(title='Pong!', description=':ping_pong:!', footer=re)
        await ctx.send(embed=e)

def setup(bot):
    bot.add_cog(AdminCommands(bot))
