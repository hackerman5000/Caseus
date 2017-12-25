""" Contains VC/Music related features """
import asyncio
import discord
import discord.ext.commands as commands
from discord import Embed
from discord import opus


class VCAndMusic:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def connect(self, ctx):
        """Connects to a Voice Channel."""

        if discord.opus.is_loaded():
            print("Opus is loaded...")
        else:
            for opus_lib in ['libopus-0.x86.dll', 'libopus-0.x64.dll', 'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']:
                try:
                    discord.opus.load_opus(opus_lib)
                except OSError:
                    pass

        if ctx.message.author.voice is None:
            await ctx.send(embed=Embed(title=":(",
                                       description="Please Join a Voice Channel before using this command...",
                                       color=discord.Color.dark_orange()
                                       ))
        else:
            await ctx.author.voice.channel.connect()
            await ctx.send(embed=Embed(title="Connecting...",
                                       color=discord.Color.dark_magenta()))

    @commands.command()
    async def disconnect(self, ctx):
        """Disconnect from a Voice Channel"""
        await ctx.user.voice.channel.disconnect()
        await ctx.send(embed=Embed(title=">Disconnected<",
                                   color=discord.Color.dark_red()))
 
def setup(bot):
    bot.add_cog(VCAndMusic(bot))
