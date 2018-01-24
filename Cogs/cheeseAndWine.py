########################################################################################################################
#                                                   COMMANDS                                                           #
########################################################################################################################
""" Contains all 'Social' commands (c#wine, c#lmgtfy, c#cheese, c#pun .etc). """
import urllib
import discord
import random
import discord.ext.commands as commands
from discord import Embed
from time import sleep


class CheeseAndWine:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cheese(self, ctx, member: discord.Member):
        """ Give someone a nice slice of cheese. """
        if member.id == ctx.bot.user.id:
            description = f"***Thank you, {ctx.author.mention} for the :cheese:!***"
        else:
            if member.id != ctx.message.author.id:
                target_mention = f'<@{member.id}>'
                description = f'***{ctx.author.mention} has given {target_mention} some :cheese:!***'
            else:
                description = f"***{ctx.author.mention}, You can't just give :cheese: to yourself!***"
        await ctx.send(embed=Embed(title="Cheese!", description=description, color=discord.Color.gold()))

    @commands.command()
    async def choose(self, ctx, *choices: str):
        """Chooses between multiple choices."""
        await ctx.send(embed=Embed(title="I Choose...", description=random.choice(choices).title(), color=discord.Color.gold()))

    @commands.command()
    async def flip(self, ctx):
        """ Flips a coin! """
        await ctx.send(embed=Embed(title="Flipping Coin...", description=random.choice(["Heads!", "Tails!"]), color=discord.Color.gold()))

    @commands.command()
    async def lmgtfy(self, ctx, *, link: str):
        """ Let the Bot google that for you."""
        link = urllib.parse.quote(link, safe='')
        await ctx.send(embed=Embed(title="One Freshly Baked Query(TM) coming right up!", 
                                   description=f"http://lmgtfy.com/?q={link}", 
                                   color=discord.Color.gold()))

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
        r_pun = random.choice(cheese_puns).split('\n')
        await ctx.send(embed=discord.Embed(title=r_pun[0], description=f"***{r_pun[-1]}***", color=discord.Color.dark_gold()))

    @commands.command()
    async def wine(self, ctx, user: discord.User):
        """ Give someone a nice (non-alcoholic) glass of wine. """
        footer = ""
        
        if user.id == ctx.bot.user.id:
            description = f"*** Thanks for the :wine_glass:, {ctx.author.mention}***"
        else:
            if user.id != ctx.author.id:
                from WineRecords import main
                description = f"***{ctx.author.mention} has given {user.mention} a glass of :wine_glass:!***"
                footer = main(ctx)
            else:
                description = f"***{ctx.author.mention}, You can't just give :wine_glass: to yourself!***"
            await ctx.send(embed=discord.Embed(description=f'{description}\n{footer}', color=discord.Color.dark_red))


def setup(bot):
    bot.add_cog(CheeseAndWine(bot))
