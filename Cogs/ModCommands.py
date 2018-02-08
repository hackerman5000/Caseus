""" Contains admin only commands, c#clear, c#ping .etc... """
import asyncio
import datetime
import inspect
import io
import os
import textwrap
import traceback
from contextlib import redirect_stdout
from time import sleep, strftime

import discord
import discord.ext.commands as commands
from discord.embeds import Embed
from discord.ext.commands import BucketType


class ModCommands:
    ''' Contains commands to be used on Members of a guild by the 'staff'. '''

    #######################################
    #           Dunder Methods            #
    #######################################

    def __init__(self, caseus: commands.bot):
        '''Stuff'''
        self.caseus = caseus

    #########################################
    #              Commands                 #
    #########################################

    @commands.command(hidden=True)
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, number: int):
        """ Clears 'n' messages from current channel. """
        await ctx.channel.purge(limit=number + 1)

    @commands.cooldown(rate=1, per=150, type=BucketType.guild)
    @commands.command()
    async def help(self, ctx):
        """ Shows this message. """
        msg = await ctx.send(embed=Embed(title='Loading Help...', color=discord.Color.dark_magenta()))
        e = Embed(title='Dunno who call? c#help!', color=discord.Color.magenta(),
                  description='The prefix \'c#\' must be used before any command.')

        for command_obj in self.caseus.all_commands.values():
            if not command_obj.hidden:
                e.add_field(name=f'{command_obj.name.title()}',
                            value=f'{command_obj.help}',
                            inline=False
                            )
        await msg.edit(embed=e)

    @commands.command()
    async def profile(self, ctx, usr: discord.Member):
        """ Gets a Member's profile. """
        from WineRecords import WineRecords
        try:
            wine = WineRecords[str(usr.id)]
        except KeyError:
            wine = 0
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
        bot.add_cog(ModCommands(bot))
