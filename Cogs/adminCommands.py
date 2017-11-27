""" Contains admin only commands, c#clear, c#ping .etc... """
import asyncio
import discord
import inspect
import discord.ext.commands as commands
from discord.ext.commands import BucketType
from discord.embeds import Embed
from HelperFunctions.EmbedGenerator import EmbGen
from time import sleep
import datetime


class AdminCommands:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, number: int):
        """ Clears chat log 'n' messages."""
        await ctx.channel.purge(limit=number+1)

    @commands.command(hidden=True)
    @commands.has_permissions(administrator=True)
    async def debug(self, ctx, *, code: str):
        """Evaluates code. [Credit to Rapptz/Danny]"""
        code = code.strip('` ')
        python = '```py\n{}\n```'
        result = None

        env = {
            'bot': self.bot,
            'ctx': ctx,
            'message': ctx.message,
            'server': ctx.message.guild,
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
                title='Exception Raised...',
                description=(python.format(type(e).__name__+":"+str(e))),
                color=discord.Color.dark_red()
            ))
            return
        else:
            await ctx.send(embed=Embed(
                title='Code Evaluated...',
                description=result,
                color=discord.Color.green()
            ))
            return
        
    @commands.cooldown(rate=1, per=150, type=BucketType.guild)
    @commands.command()
    async def help(self, ctx):
        """ Shows this message. """
        msg = await ctx.send(embed=Embed(title='Loading Help...', color=discord.Color.dark_magenta()))
        e = Embed(title='Dunno who call? c#help!', color=discord.Color.magenta(),
                  description='The prefix \'c#\' must be used before any command.')
        for command_obj in self.bot.all_commands.values():
            if not command_obj.hidden:
                e.add_field(name=f'{command_obj.name.title()}',
                            value=f'{command_obj.help}',
                            inline=False)
        await msg.edit(embed=e)

    @commands.command(hidden=True)
    async def ping(self, ctx):
        """ Tests self.bot Functionality """
        re = f'Responded in {round(self.bot.latency, 2)} microseconds.'
        e = EmbGen(title='Pong!', description=':ping_pong:!', footer=re)
        await ctx.send(embed=e)
    
    @commands.command(hidden=True)
    @commands.has_permissions(manage_messages=True)
    async def silence(self, ctx, usr: discord.Member, sec: int):
        """ Silence a User for {sec} seconds. """
        if 'Muted' not in [role.name for role in ctx.message.guild.roles]:
            await ctx.message.guild.create_role(name='Muted',
                                                color=discord.Color.red(),
                                                mentionable=True)
        muted = discord.utils.get(ctx.message.guild.roles, name='Muted')
        await usr.add_roles(muted)
        asyncio.sleep(sec)
        await usr.remove_roles(muted)
        await ctx.send(embed=Embed(title=':)',
                                   description=f"Hope you've learnt your Lesson, {usr.mention}",
                                   color=discord.Color.gold()), delete_after=5)
        
def setup(bot):
    bot.add_cog(AdminCommands(bot))
