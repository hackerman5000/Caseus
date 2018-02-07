"""
This file serves as the 'entry point' for the bot.

It also handles:
        -> Exceptions during Cog loading and command execution;
        -> Events;

"""
import os
from glob import glob

import discord
from discord import Embed
from discord.ext import commands

######################
#         Enviromental Vars            #
######################


PREFIX: str = os.getenv('PREFIX')
VERSION: str = os.getenv('HEROKU_RELEASE_VERSION')
TOKEN: str = os.getenv('BOT_TOKEN')
OWNER_ID: int = os.getenv('OWNER_ID')

Caseus = commands.bot(
    command_prefix=PREFIX,
    pm_help=None,
    owner_id=OWNER_ID
)
Caseus.remove_command('help')


######################
# -- Events and Error Handlng --#
######################


@Caseus.event
async def on_ready():
    """ On Startup, The Caseus prints the following to the console. """
    global version
    print("Name: {}".format(Caseus.user.name))
    print("Version: {}".format(version))
    print("ID: {}".format(Caseus.user.id))
    await Caseus.change_presence(game=discord.Game(name="Grating Cheese(c#help)"))


@Caseus.event
async def on_command_error(ctx, error):
    """ Runs this block on Errors. """
    print(f"Error raised by {ctx.author.name}[{ctx.guild.name}] using {ctx.message.content}")
    print(str(error))
    await ctx.send(embed=Embed(
        title="An Error has occured...",
        description=f"***{str(error)}***",
        color=discord.Color.red()))


@Caseus.before_invoke
async def BeforeInvoke(ctx):
    """ Runs this block of code before invokation. """
    await ctx.message.add_reaction(u"\U0001F9C0")
    print(f"{ctx.author.name}[{ctx.guild.name}] invoked the command {ctx.message.content}.")

if __name__ == '__main__':
    os.chdir('Cogs')
    for cog in glob("*.py"):
        try:
            Caseus.load_extension(cog)
        except Exception as e:
            print(f'Failed to load extension {cog}.')
            print(f"Exception:\n{str(e)}")

Caseus.run(TOKEN)
