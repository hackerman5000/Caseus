import discord
import random
import urllib
import os
import sys
from time import sleep
from discord.ext import commands

prefix = 'c#'  # Use this to 'command' a bot.
version = '1.5'
bot_token = os.getenv('bot_token')

# Initiates the Bot class, Detailing the prefix.
bot = commands.Bot(command_prefix=prefix, description='Bonjour Monsieur / Madame.\n', pm_help=True)

'''
TODO    
- Implement Voice/Music capabilities
- Implement more 'interactive' functions (c#cake, c#shit, c#liquidass).
'''

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
    await bot.change_presence(game=discord.Game(name="Grating Cheese"))


########################################################################################################################
#                                                    UTILITY//FUN                                                      #
########################################################################################################################


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
        if user_name.id in usr_list and user_name.id != author.id:
            target_mention = '<@{}>'.format(user_name.id)
            await bot.say('{0} has given {1} some :cheese:!'.format(author_mention, target_mention))
        else:
            await bot.say("{}, You can't just give :cheese: to yourself!".format(author_mention))


@bot.command(pass_context=True)
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await bot.add_reaction(ctx.message, u"\U0001F9C0")
    await bot.say(random.choice(choices))

    
    
@commands.has_permissions()
@bot.command(pass_context=True, hidden=True)
async def clear(ctx, number):
    """ Clears chat log 'n' messages."""
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


@commands.has_permissions()
@bot.command(pass_context=True, hidden=True)
async def crash(ctx):
    """ Induces a crash [Only usable by NN/SC & gum]. """
    if ctx.message.author.id == "205633407093309440" or ctx.message.author.id == "281120477945266177":
        await bot.say("Goodbye Cruel World...")
        sys.exit()
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

    

@commands.has_permissions()
@bot.command(pass_context=True)
async def python(ctx):
    """ Interprets Python Code and gets the result from repl.it/python3 """
    await bot.say("***This has'nt been implemented yet and is still in EXTREMELY early WIP.***")
                  
               

@bot.command(pass_context=True)
async def lmgtfy(ctx, link):
    """ Let the bot google that for you...\nJust make sure to use quotes around multi-word searches."""
    link = urllib.parse.quote(link, safe='')
    await bot.add_reaction(ctx.message, u"\U0001F9C0")
    await bot.say("```[One Freshly Baked Query:tm: comming right up!]http://lmgtfy.com/?q={}".format(link))
    sleep(1)


@commands.has_permissions()
@bot.command(pass_context=True, hidden=True)
async def ping(ctx):
    """ Tests Bot Functionality """
    print("Pinged by..." + ctx.message.author.name)
    msg = ctx.message
    author_mention = '<@{}>'.format(ctx.message.author.id)
    await bot.add_reaction(msg, u"\U0001F9C0")
    await bot.say("{} Pong! :ping_pong:".format(author_mention))
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


@commands.has_permissions()
@bot.command(pass_context=True, hidden=True)
async def ver(ctx):
    """ Print Version Control and Console """
    global version
    await bot.add_reaction(ctx.message, u"\U0001F9C0")
    await bot.say("Hello World!\nCeaseus V{} reporting for duty...".format(version))

@bot.command(pass_context=True)
async def wine(ctx, user_name: discord.User):
    """ Give someone a nice (non-alcoholic) glass of wine. """
    title = ctx.message.content
    description = ""
    footer = ""

    usr_list = []
    author = ctx.message.author
    author_mention = '<@{}>'.format(author.id)
    await bot.add_reaction(ctx.message, u"\U0001F377")  # <-- Wine Emoji - UTF-8.

    for member in ctx.message.server.members:
        usr_list.append(member.id)

    else:
        if user_name.id == "369099294579359744":
            description = "Thanks for the :wine_glass:, {}!".format(author_mention)

        else:
            if user_name.id in usr_list and user_name.id != author.id:

                from WineRecords import main
                target_mention = '<@{}>'.format(user_name.id)
                description = '{0} has given {1} a glass of :wine_glass:!'.format(author_mention, target_mention)
                footer = main(user_name.id)

            else:
                description = "{}, You can't just give :wine_glass: to yourself!".format(author_mention)

        embed = discord.Embed(title=title,
                              description=description,
                              color=0xff8040)
        embed.set_footer(text=footer)
        await bot.say("Something", embed=embed)

bot.run(bot_token)
