""" Contains admin only commands, c#clear, c#ping .etc... """
import os
import asyncio
import discord
import inspect
import discord.ext.commands as commands
from WineRecords import main
from discord.ext.commands import BucketType
from discord.embeds import Embed
from time import sleep, strftime
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
                e.add_field(name='\u200b', value='\u200b')
        await msg.edit(embed=e)

    @commands.command(hidden=True)
    async def ping(self, ctx):
        """ Tests self.bot Functionality """
        version = os.getenv('HEROKU_RELEASE_VERSION')
        e = Embed(title='Pong!', description=':ping_pong:!', color=discord.Color.green())
        e.add_field(name="Latency:", value=f"Responded in {round(self.bot.latency, 2)} microseconds.")
        e.set_footer(text=f"Caseus Version {version}")
        await ctx.send(embed=e)

    @commands.command()
    async def profile(self, ctx, usr: discord.Member):
        """Gets a User's/Member's profile."""
        wine = main(usr.id)
        joined_at = usr.joined_at.strftime('%B-%d-%Y|%I:%M%p')
        last_message = await ctx.channel.history().get(author__name=f'{usr.name}')
        profile = Embed(title=f"{usr.name}'s Profile",
                        color=usr.color)
        profile.set_thumbnail(url=usr.avatar_url_as(static_format='png', size=256))
        profile.add_field(name='\u200b', value='\u200b')
        profile.add_field(name='Role:', value=f"{usr.top_role}")
        profile.add_field(name="Joined at:",
                          value=f"{joined_at}",
                          inline=True)
        profile.add_field(name='Glasses of Wine given:', value=f'{wine}')
        await ctx.send(embed=profile)
    
    @commands.command(hidden=True)
    @commands.has_permissions(administrator=True)
    async def silence(self, ctx, usr: discord.Member, sec: int):
        """ Silence a User for {sec} seconds. """
        if 'Muted' not in [role.name for role in ctx.message.guild.roles]:
            await ctx.message.guild.create_role(name='Muted',
                                                color=discord.Color.red(),
                                                mentionable=True)
        usr_roles = usr.roles[1::]
        muted = discord.utils.get(ctx.message.guild.roles, name='Muted')
        await usr.add_roles(muted)
        await ctx.message.delete()
        
        for role in usr_roles:
            await usr.remove_roles(role)
        await asyncio.sleep(sec)
        await usr.remove_roles(muted)

        for role in usr_roles:
            await usr.add_roles(role)
        await ctx.send(embed=Embed(title=':)',
                                   description=f"Hope you've learnt your Lesson, {usr.mention}",
                                   color=discord.Color.gold()), delete_after=5)

 
def setup(bot):
    bot.add_cog(AdminCommands(bot))
