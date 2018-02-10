import asyncio
import datetime
import inspect
import io
import os
import textwrap
import traceback
from contextlib import redirect_stdout
from time import sleep, strftime

import discord
import discord.ext.commands as commands
from discord.embeds import Embed
from discord.ext.commands import BucketType


class AgCommands:
        '''Contains commands that *should* only be used by the owner of the bot'''

        #######################################
        #           Dunder Methods            #
        #######################################

        def __init__(self, cas):
            '''Stuff'''
            self.cas = cas

        ##########################################
        #           Static Methods               #
        ##########################################

        @staticmethod
        def CleanupCode(content: str) -> str:
            """Automatically removes code blocks from the code."""
            # Remove ```py\n```
            if content.startswith('```') and content.endswith('```'):
                return '\n'.join(content.split('\n')[1:-1])

            # Remove `foo`
            return content.strip('` \n')

        #########################################
        #              Commands                 #
        #########################################
        
        @commands.command(hidden=True)
        @commands.is_owner()
        async def WineDB(self, ctx):
            '''Send a 'copy' of the DB if needed.'''
            from WineRecords import WineRecords
            await self.caseus.get_user(self.caseus.owner_id).send(WineRecords)

        @commands.command(hidden=True)
        @commands.is_owner()
        async def debug(self, ctx, *, body: str):
            '''Evaluates a chunk of code.'''
            env = {
            'cas': self.cas,
            'ctx': ctx,
            }.update(globals())

            body = self.CleanupCode(body)
            stdout = io.StringIO()
            toCompile = f'async def func():\n{textwrap.indent(body, "  ")}'

            try:
                exec(toCompile, env)
            except Exception as e:
                return await ctx.send(Embed(title="Exception:",
                                                description=f"```py\n{e.__class__.__name__}{e}\n```",
                                                color=discord.Color.dark_red))
            func = env['func']
            try:
                with redirect_stdout(stdout):
                 ret = await func()

            except Exception as e:
                 value = stdout.getvalue()
                 await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')

            else:
                 value = stdout.getvalue()
                 if ret is None:
                        if value:
                            await ctx.send(f'```py\n{value}\n```')
          
                        else:
                            self._last_result = ret
                            await ctx.send(f'```py\n{value}{ret}\n```')

        @commands.command(hidden=True)
        async def ping(self, ctx):
            """ Tests Functionality """
            VERSION = os.getenv('HEROKU_RELEASE_VERSION')
            e = Embed(title='Pong!', description=':ping_pong:!', color=discord.Color.green())
            e.set_footer(text=f"Caseus Version {VERSION}")
            e.add_field(name="Latency:", value=f"Responded in {round(self.cas.latency, 2)} microseconds.")
            await ctx.send(embed=e)

def setup(bot):
        bot.add_cog(AgCommands(bot))
