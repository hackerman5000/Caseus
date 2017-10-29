import os
import discord
from HelperFunctions.EmbedGenerator import EmbGen
from discord.ext import commands

prefix = 'c#'  # Use this to 'command' a bot.
version = '1.75.1'
bot_token = os.getenv('bot_token')

# Initiates the Bot class, Detailing the prefix.
# Initiates the Bot class, Detailing the prefix.
bot = commands.Bot(command_prefix=prefix,
                   description='Bonjour Monsieur / Madame.\n',
                   pm_help=None,
                   command_not_found=EmbGen(title="Command not found!",
                                            description="That command does not exist, Try again!"),
                   owner_id="205633407093309440"
        )
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
async def on_command_error(event, *args):
    """When an Error is raised, The Bot prints and Informs the following to the console."""
    from traceback import format_exc
    message = args[0]
    desc=format_exc()
    await bot.say(embed=EmbGen(title="Error!",
                               description="{} has resulted in the following error:\n{}".format(message,desc)
                               )
    
@bot.command()
async def load(extension_name: str):
    """Loads up a cog."""
    try:
        bot.load_extension(extension_name)
    except Exception as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await bot.say("Extension {} loaded.".format(extension_name))


@bot.command()
async def unload(extension_name: str):
    """Unloads a cog."""
    bot.unload_extension(extension_name)
    await bot.say("Extension {} unloaded.".format(extension_name))

if __name__ == "__main__":
    for extension in Extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

bot.run(bot_token)
