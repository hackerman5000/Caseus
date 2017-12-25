import os
import discord
from discord import Embed
from discord.ext import commands

prefix = 'c#'  # Use this to 'command' a bot.
version = os.getenv('HEROKU_RELEASE_VERSION')
bot_token = os.getenv('bot_token')

# Initiates the Bot class, Detailing the prefix.
bot = commands.Bot(command_prefix=prefix,
                   description='Bonjour Monsieur / Madame.\n',
                   pm_help=None,
                   owner_id=205633407093309440
                   )
bot.remove_command('help')

# These are the extensions (cogs).
Extensions = ["Cogs.adminCommands", "Cogs.cheeseAndWine", "Cogs.vcAndMusic"]


########################################################################################################################
#                                                        STARTUP                                                       #
########################################################################################################################


@bot.event
async def on_ready():
    """On Startup, The Bot prints the following to the console."""
    global version
    print("Name: {}".format(bot.user.name))
    print("Version: {}".format(version))
    print("ID: {}".format(bot.user.id))
    await bot.change_presence(game=discord.Game(name="Grating Cheese(c#help)"))


@bot.event
async def on_command_error(ctx, error):
    """ Runs this block on Errors. """
    print(f"Error raised by {ctx.author.name}[{ctx.guild.name}] using {ctx.message.content}")
    await ctx.send(embed=discord.Embed(
        title="An Error has occured...",
        description=f"***{str(error).title()}***",
        color=discord.Color.red()))


@bot.before_invoke
async def BeforeInvoke(ctx):
    """ Runs this block of code before invokation. """
    await ctx.message.add_reaction(u"\U0001F9C0")
    print(f"{ctx.author.name}[{ctx.guild.name}] invoked the command {ctx.message.content}.")

if __name__ == '__main__':
    for extension in Extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.')
    if discord.opus.is_loaded():
        print("Opus is loaded...")
    else:
        for opus_lib in ['libopus-0.x86.dll', 'libopus-0.x64.dll', 'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']:
            try:
                discord.opus.load_opus(opus_lib)
            except OSError:
                pass
        print(f"Could not load an opus lib. Tried {opus_libs}")

bot.run(bot_token)
