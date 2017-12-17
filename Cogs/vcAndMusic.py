""" Contains VC/Music related features """
import asyncio
import discord
import discord.ext.commands as commands
from discord import Embed


class VCAndMusic:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def connect(self, ctx):
        """Connects to a Voice Channel."""
        if ctx.message.author.voice is None:
            await ctx.send(embed=Embed(title=":(",
                                       description="Please Join a Voice Channel before using this command...",
                                       color=discord.Color.dark_orange()
                                       ))
        else:
            await ctx.author.voice.voice_channel.connect()
            await ctx.send(embed=Embed(title="Connecting...",
                                       color=discord.Color.dark_magenta()))

    @commands.command()
    async def disconnect(self, ctx):
        """Disconnect from a Voice Channel"""
        await ctx.user.voice.voice_channel.disconnect()
        await ctx.send(embed=Embed(title=">Disconnected<",
                                   color=discord.Color.dark_red()))
 
def setup(bot):
    bot.add_cog(VCAndMusic(bot))
