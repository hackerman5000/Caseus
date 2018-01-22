""" Contains admin only commands, c#clear, c#ping .etc... """
import asyncio
import datetime
import inspect
import io
import textwrap
import os
from contextlib import redirect_stdout
from time import sleep, strftime

import traceback
import discord
import discord.ext.commands as commands
from discord.embeds import Embed
from discord.ext.commands import BucketType

from WineRecords import main


class AdminCommands:
    def __init__(self, bot):
        self.bot = bot
        self._last_result = None
    
    def cleanup_code(self, content):
        """Automatically removes code blocks from the code."""
        # remove ```py\n```
        if content.startswith('```') and content.endswith('```'):
            return '\n'.join(content.split('\n')[1:-1])

        # remove `foo`
        return content.strip('` \n')

    @commands.command(hidden=True)
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, number: int):
        """ Clears chat log 'n' messages."""
        await ctx.channel.purge(limit=number + 1)

    @commands.command(hidden=True, name='eval')
    @commands.is_owner()
    async def _eval(self, ctx, *, body: str):
        """Evaluates a code"""

        env = {
            'bot': self.bot,
            'ctx': ctx,
            'channel': ctx.channel,
            'author': ctx.author,
            'guild': ctx.guild,
            'message': ctx.message,
            '_': self._last_result
        }

        env.update(globals())

        body = self.cleanup_code(body)
        stdout = io.StringIO()

        to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

        try:
            exec(to_compile, env)
        except Exception as e:
            return await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')

        func = env['func']
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except Exception as e:
            value = stdout.getvalue()
            await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
        else:
            value = stdout.getvalue()
            try:
                await ctx.message.add_reaction('\u2705')
            except:
                pass

            if ret is None:
                if value:
                    await ctx.send(f'```py\n{value}\n```')
            else:
                self._last_result = ret
                await ctx.send(f'```py\n{value}{ret}\n```')

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
        profile = Embed(title=f"{usr.name}'s Profile",
                        color=usr.color)
        profile.set_thumbnail(url=usr.avatar_url_as(static_format='png', size=256))
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
