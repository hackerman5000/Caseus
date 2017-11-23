########################################################################################################################
#                                                   COMMANDS                                                           #
########################################################################################################################
""" Contains all 'Social' commands (c#wine, c#lmgtfy, c#cheese, c#pun .etc). """
import urllib
import discord
import random
import discord.ext.commands as commands
from HelperFunctions.EmbedGenerator import EmbGen
from time import sleep


class CheeseAndWine:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cheese(self, ctx, member: discord.Member):
        """ Give someone a nice slice of cheese. """
        usr_list = []
        author_mention = '<@{}>'.format(ctx.author.id)

        for guild_member in ctx.message.guild.members:
            usr_list.append(guild_member.id)

        if member.id == ctx.bot.user.id:
            description = ("***Thank you, {} for the :cheese:!***".format(author_mention))
        else:
            if member.id in usr_list and member.id != ctx.message.author.id:
                target_mention = '<@{}>'.format(member.id)
                description = '***{0} has given {1} some :cheese:!***'.format(author_mention, target_mention)
            else:
                description = "***{}, You can't just give :cheese: to yourself!***".format(author_mention)
        await ctx.send(embed=EmbGen(title="Cheese!", description=description))

    @commands.command()
    async def choose(self, ctx, *choices: str):
        """Chooses between multiple choices."""
        await ctx.send(embed=EmbGen(title="I Choose...", description=random.choice(choices).title()))

    @commands.command()
    async def flip(self, ctx):
        """ Flips a coin! """
        print("Flipping Coin...")
        await ctx.send(embed=EmbGen(title="Flipping Coin...",
                                   description="Heads!" if random.randint(0, 1) == 1 else "Tails!"))
        sleep(1)

    @commands.command()
    async def lmgtfy(self, ctx, *, link: str):
        """ Let the self.bot google that for you...\nJust make sure to use quotes around multi-word searches."""
        link = urllib.parse.quote(link, safe='')
        await ctx.send(embed=EmbGen(
                    title="One Freshly Baked Query(TM) coming right up!",
                    description="http://lmgtfy.com/?q={}".format(link)
                                  )
                           )

    @commands.command()
    async def pun(self, ctx):
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
        r_pun = random.choice(cheese_puns).split('\n')
        await ctx.send(embed=EmbGen(title=r_pun[0], description="***{}***".format(r_pun[-1])))

    @commands.command()
    async def wine(self, ctx, user_name: discord.User):
        """ Give someone a nice (non-alcoholic) glass of wine. """
        footer = ""
        usr_list = []
        author = ctx.message.author
        author_mention = ctx.message.author.mention

        for member in ctx.message.guild.members:
            usr_list.append(member.id)
        else:
            if user_name.id == ctx.bot.user.id:
                description = "***Thanks for the :wine_glass:, {}!***".format(author_mention)
    
            else:
                if user_name.id in usr_list and user_name.id != author.id:
                    from WineRecords import main
                    target_mention = user_name.mention
                    description = '***{0} has given {1} a glass of :wine_glass:!***'.format(author_mention,
                                                                                            target_mention)
                    footer = main(user_name.id)
    
                else:
                    description = "***{}, You can't just give :wine_glass: to yourself!***".format(author_mention)
            await ctx.send(embed=EmbGen(description=description + "\n" + footer))


def setup(bot):
    bot.add_cog(CheeseAndWine(bot))
