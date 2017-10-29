""" Contains VC/Music related features """
import discord.ext.commands as commands


class VCAndMusic:
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(pass_context=True)
    async def connect(self, ctx):
        """ Connect to a voice server. """
        if self.bot.is_voice_connected(self, ctx.message.server):
            return await self.bot.say("I am already connected to a voice channel. Do not disconnect me if I am in use!")
        author = ctx.message.author
        voice_channel = author.voice_channel
        await self.bot.join_voice_channel(voice_channel)

    @commands.command(pass_context=True)
    async def disconnect(self, ctx):
        """ Disconnect from a voice server"""
        for x in self.bot.voice_clients:
            if x.server == ctx.message.server:
                return await x.disconnect()


def setup(bot):
    bot.add_cog(VCAndMusic(bot))
