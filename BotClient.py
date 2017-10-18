import discord
import random
import urllib
from time import sleep
from discord.ext import commands

Client = discord.Client()  # Creates a new Discord clients.
prefix = 'c#'  # Use this to 'command' a bot.
version = '1'.zfill(2)

'''
TODO 
- Implement more 'interactive' functions (c#cake, c#shit, c#liquidass).
- Implement Voice/Music capabilities
'''

# Initiates the Bot class, Detailing the prefix.
bot = commands.Bot(command_prefix=prefix, description='Bonjour Monsieur / Madame.\n', pm_help=True)


#########################################################################################################
@bot.event
async def on_ready():
    """On Startup, The Bot prints the following to the console."""
    global version
    print("Name: {}".format(bot.user.name))
    print("Version: {}".format(version))
    print("ID: {}".format(bot.user.id))
    await bot.change_presence(game=discord.Game(name='Grating Cheese(c#help)'))


@bot.command(pass_context=True, hidden=True)
async def ver(ctx):
    """ Print Version Control and Console """
    global version
    await bot.add_reaction(ctx.message, u"\U0001F9C0")
    await bot.say("Hello World!\nCeaseus V{} reporting for duty...".format(version))


#########################################################################################################


@bot.command(pass_context=True)
async def cheese(ctx, user_name: discord.User):
    """ Give someone a nice slice of cheese. """
    usr_list = []
    author = ctx.message.author
    author_mention = '<@{}>'.format(author.id)
    await bot.add_reaction(ctx.message, u"\U0001F9C0")

    for member in ctx.message.server.members:
        usr_list.append(member.id)

    if user_name.id == "369099294579359744":
        await bot.say("Thank you, {} for the :cheese:!".format(author_mention))
    else:
        if user_name.id in usr_list:
            target_mention = '<@{}>'.format(user_name.id)
            await bot.say('{0} has given {1} some :cheese:!'.format(author_mention, target_mention))
        else:
            await bot.say("{}, You can't just give :cheese: to people who don't exist!".format(author_mention))


@bot.command(pass_context=True, description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await bot.add_reaction(ctx.message, u"\U0001F9C0")
    await bot.say(random.choice(choices))


@bot.command(pass_context=True, hidden=True)
async def clear(ctx, number):
    """ Clears chat log 'n' messages."""
    if ctx.message.author.role is
        mgs = []
    number = int(number)  # Converting the amount of messages to delete to an integer
    async for x in bot.logs_from(ctx.message.channel, limit=number):
        mgs.append(x)
    await bot.delete_messages(mgs)


@bot.command(pass_context=True)
async def connect(ctx):
    """ Connect to a voice server. """
    if bot.is_voice_connected(ctx.message.server):
        return await bot.say("I am already connected to a voice channel. Do not disconnect me if I am in use!")
    author = ctx.message.author
    voice_channel = author.voice_channel
    await bot.join_voice_channel(voice_channel)


@bot.command(pass_context=True, hidden=True)
async def crash(ctx):
    """ Induces a crash [Only usable by NN/SC]. """
    if ctx.message.author.id == "205633407093309440":
        await bot.say("Goodbye Cruel World...")

    else:
        await bot.say("You do not have permissions to make me crash.")


@bot.command(pass_context=True)
async def disconnect(ctx):
    """ Disconnect from a voice server"""
    for x in bot.voice_clients:
        if x.server == ctx.message.server:
            return await x.disconnect()


@bot.command(pass_context=True)
async def flip(ctx):
    """ Flips a coin! """
    print("Flipping Coin...")
    await bot.add_reaction(ctx.message, u"\U0001F9C0")
    await bot.say("Flipping Coin...")
    await bot.say('Heads!') if random.randint(0, 1) == 1 else bot.say('Tails!')
    sleep(1)


@bot.command(pass_context=True)
async def lmgtfy(ctx, link):
    """ Let the bot google that for you...\nJust make sure to use quotes around multi-word searches."""
    link = urllib.parse.quote(link, safe='')
    await bot.add_reaction(ctx.message, u"\U0001F9C0")
    await bot.say("http://lmgtfy.com/?q={}".format(link))
    sleep(1)


@bot.command(pass_context=True, hidden=True)
async def ping(ctx):
    """ Tests Bot Functionality """
    print("Pinged by..." + ctx.message.author.name)
    msg = ctx.message
    await bot.add_reaction(msg, u"\U0001F9C0")
    await bot.say("Please...{} don't ping me ***that hard ***...".format(ctx.message.author.name))
    sleep(1)


@bot.command(pass_context=True)
async def pun(ctx):
    """ Produces 'freshly' fermented Cheese Puns."""
    cheese_puns = [
        "What does cheese say when it looks in the mirror?\nHalloumi!",
        "What cheese can be used to encourage a bear?\nCamembert!",
        "What cheese has a bit of an alcohol problem?\nLivarot!",
        "What cheese can be used to hide a horse?\nMascsarpone!",
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
    print("Saying Pun...")
    await bot.add_reaction(ctx.message, u"\U0001F9C0")
    await bot.say(cheese_puns[random.randint(0, len(cheese_puns) - 1)])
    sleep(1)


bot.run('TOKEN')
