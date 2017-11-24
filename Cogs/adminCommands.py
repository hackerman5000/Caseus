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
    async def debug(self, ctx, *, code: str):
        """Evaluates code."""
        
        code = code.strip('` ')
        python = '```py\n{}\n```'
        result = None
        env = {
            'bot': self.bot,
            'ctx': ctx,
            'message': ctx.message,
            'server': ctx.message.server,
            'channel': ctx.message.channel,
            'author': ctx.message.author
        }
        
        env.update(globals())

        try:
            result = eval(code, env)
            if inspect.isawaitable(result):
                result = await result
        except Exception as e:
            await ctx.send(embed=Embed(
                title='Exception Raised:',
                description=python.format(type(e).__name__+ ": " + str(e)),
                color=discord.Color.dark_red()
            ))
            return

        await ctx.send(embed=Embed(
            title="stdout",
            description=python.format(result),
            color=discord.Color.green()
        ))
        await self.bot.say(python.format(result))

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
