import random
import urllib
from time import sleep

import discord
import discord.ext.commands as commands
from discord import Embed


class MiscCommands:
    '''Contains Misc commands.'''

    #######################################
    #           Dunder Methods            #
    #######################################

    def __init__(self, caseus: commands.bot):
        '''Stuff'''
        self.caseus = caseus

    #########################################
    #               Commands                #
    #########################################

    @commands.command()
    async def cheese(self, ctx, member: discord.Member):
        """ Give someone a nice slice of cheese. """
        if member.id == ctx.bot.user.id:
            description = f"***Thank you, {ctx.author.mention} for the :cheese:!***"
        else:
            if member.id != ctx.message.author.id:
                description = f'***{ctx.author.mention} has given {member.mention} some :cheese:!***'
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
            from WineRecords import WineRecords
            if user.id != ctx.author.id:
                try:
                    WineRecords[str(user.id)] += 1
                except KeyError:
                    WineRecords[str(user.id)] = 1
                description = f"***{ctx.author.mention} has given {user.mention} a glass of :wine_glass:!***"
                footer = f"*{user.mention} has been given {WineRecords[str(user.id)]} glasses of :wine_glass:!*"
            else:
                description = f"***{ctx.author.mention}, You can't just give :wine_glass: to yourself!***"
            await ctx.send(embed=discord.Embed(description=f'{description}\n{footer}', color=discord.Color.dark_red()))


setup = lambda cas: cas.add_cog(MiscCommands(cas))
