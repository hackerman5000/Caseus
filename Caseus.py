"""
This file serves as the 'entry point' for the bot.

It also handles:
        -> Exceptions during Cog loading and command execution;
        -> Events;

"""
import os
import discord
from discord import Embed
from discord.ext import commands

########################################
#         Enviromental Vars            #
########################################

Extensions = ['Cogs.AgCommands', 'Cogs.MiscCommands', 'Cogs.ModCommands']
PREFIX = os.getenv('PREFIX')
VERSION = os.getenv('HEROKU_RELEASE_VERSION')
TOKEN = os.getenv('BOT_TOKEN')
OWNER_ID = int(os.getenv('OWNER_ID'))

Caseus = commands.Bot(
    command_prefix=PREFIX,
    pm_help=None,
    owner_id=OWNER_ID
)
Caseus.remove_command('help')


#################################
#  --Events and Error Handlng-- #
#################################


@Caseus.event
async def on_ready():
    """ On Startup, The Caseus prints the following to the console. """
    global VERSION
    print("Name: {}".format(Caseus.user.name))
    print("Version: {}".format(VERSION))
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

if __name__ == "__main__":
    for extension in Extensions:
        try:
            Caseus.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

Caseus.run(TOKEN)
