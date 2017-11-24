""" Contains VC/Music related features """
from discord import Embed
import discord.ext.commands as commands
import discord
import asyncio
import youtube_dl

youtube_dl.utils.bug_reports_message = lambda: ''


ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'before_options': '-nostdin',
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, ytdl.extract_info, url)

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


class VCAndMusic:
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def connect(self, ctx):
        """Connects to a voice channel"""
        
        channel = ctx.message.author.voice.voice_channel
        if ctx.voice_client is not None and channel is not None:
            ctx.send(embed=Embed(
                title="Joining Voice Channel...",
                description=f"Joining the {channel} channel",
                color=discord.Color.green()
            ))
            return await ctx.voice_client.move_to(channel)

    @commands.command()
    async def disconnect(self, ctx):
        """Disconnect from a voice channel"""
        await ctx.voice_client.disconnect()

    @commands.command()
    async def yt(self, ctx, *, url):
        """Streams from a url (almost anything youtube_dl supports)"""

        if ctx.voice_client is None:
            if ctx.author.voice.channel:
                await ctx.author.voice.channel.connect()
            else:
                return await ctx.send("Not connected to a voice channel.")

        if ctx.voice_client.is_playing():
            ctx.voice_client.stop()

        player = await YTDLSource.from_url(url, loop=self.bot.loop)
        ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

        await ctx.send(embed=Embed(
            title='Now Playing...',
            description=f'{player.title}',
            color=discord.Color.dark_red()
        ))


def setup(bot):
    bot.add_cog(VCAndMusic(bot))
