import discord
from discord.ext import commands
import random

Client = discord.Client()  # Creates a new Discord clients.
prefix = 'c#'              # Use this to 'command' a bot.

# Initiates the Bot class, Detailing the prefix.
bot = commands.Bot(command_prefix=prefix, description='Bonjour Monsieur / Madame.\n')


@bot.event
async def on_ready():
    """On Startup, The Bot prints the following to the console."""
    print('HOHOHOHO LE BOT IS ONLINE!')
    print(bot.user.name)
    print('------')


@bot.command()
async def flip():
    """ Flips a coin! """
    await bot.say('Heads!') if random.randint(0, 1) == 1 else bot.say('Tails!')


@bot.command()
async def cheese():
    """ Produces 'freshly' fermented Cheese Puns."""
    cheese_puns = [
        "What does cheese say when it looks in the mirror?\nHalloumi!",
        "What cheese can be used to encourage a bear?\nCamembert!",
        "What cheese has a bit of an alcohol problem?\nLivarot!",
        "What cheese can be used to hide a horse?\nMascarpone!",
        "What cheese do you need to be very cautious with?\nCaerphilly!",
        "What cheese can fly?\nCurds of Prey!",
        "What's the most religious cheese?\nEmmental!",
        "What hotel does cheese stay at?\nThe Stilton!",
        "What's the saddest cheese?\nBlue Cheese!",
        "What does cheese like to drink?\nMorbier!",
        "What search engine does cheese use?\nAsk Cheese!",
        "What do you call cheese that is'nt yours?\nNacho Cheese!"
        "What genre of music does cheese listen to?\nR & Brie!",
        "What's a beaver's favorite cheese?\nEdam!",
        "What happens when cheese gets ill?\nIt gets Feta!",
        "What does cheese build when it goes to the beach?\nA Roquefort!",
        "What's the last piece of cheese left?\nForever Provolone!",
        "What's a cannibal's favorite cheese?\nLimburget!"
    ]
    await bot.say(cheese_puns[random.randint(0, len(cheese_puns)-1)])

bot.run('token[Ask for it!]')

