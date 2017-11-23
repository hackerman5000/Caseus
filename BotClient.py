import os
import discord
from HelperFunctions.EmbedGenerator import EmbGen
from discord.ext import commands

prefix = 'c#'  # Use this to 'command' a bot.
version = '1.75.1'
bot_token = os.getenv('bot_token')

# Initiates the Bot class, Detailing the prefix.
bot = commands.Bot(command_prefix=prefix,
                   description='Bonjour Monsieur / Madame.\n',
                   pm_help=None,
                   owner_id=205633407093309440
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
async def on_command_error(ctx, error):
    await ctx.send(embed=EmbGen(title="An Error has occured...",
                                description=f"***{str(error).title()}***",
                                color=discord.Color.red()))


@bot.before_invoke
async def BeforeInvoke(ctx):
    await ctx.message.add_reaction(u"\U0001F9C0")

if __name__ == '__main__':
    for extension in Extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.')


bot.run(bot_token)
