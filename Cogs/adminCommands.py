""" Contains admin only commands, c#clear, c#ping .etc... """
import discord.ext.commands as commands
from HelperFunctions.EmbedGenerator import EmbGen
from time import sleep


class AdminCommands:
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions()
    @commands.command(pass_context=True, hidden=True)
    async def clear(self, ctx, number):
        """ Clears chat log 'n' messages."""
        mgs = []
        number = int(number)  # Converting the amount of messages to delete to an integer
        async for x in self.bot.logs_from(ctx.message.channel, limit=number):
            mgs.append(x)
        await self.bot.delete_messages(mgs)

    @commands.has_permissions()
    @commands.command(pass_context=True, hidden=True)
    async def crash(self, ctx):
        """ Induces a crash [Only usable by NN/SC & gum]. """
        if ctx.message.author.id == "205633407093309440" or ctx.message.author.id == "281120477945266177":
            await self.bot.say("Goodbye Cruel World...")
            await self.bot.close()
        else:
            await self.bot.say("You do not have permissions to make me crash.")

    @commands.has_permissions()
    @commands.command(pass_context=True, hidden=True)
    async def ping(self, ctx):
        """ Tests self.bot Functionality """
        print("Pinged by..." + ctx.message.author.name)
        msg = ctx.message
        await self.bot.add_reaction(msg, u"\U0001F9C0")
        await self.bot.say(embed=EmbGen(title="Pong!", description=":ping_pong:!"))
        sleep(1)

    @commands.has_permissions()
    @commands.command(pass_context=True)
    async def python(self, ctx):
        """ Interprets Python Code and gets the result from repl.it/python3 """
        await self.bot.say("***This has'nt been implemented yet and is still in EXTREMELY early WIP.***")

    @commands.has_permissions()
    @commands.command(pass_context=True, hidden=True)
    async def ver(self, ctx):
        """ Print Version Control and Console """
        await self.bot.add_reaction(ctx.message, u"\U0001F9C0")
        await self.bot.say(embed=EmbGen(title="Hello World!",
                                        description="***Caseus v(This Is Broken) reporting for duty!***".format()))


def setup(bot):
    bot.add_cog(AdminCommands(bot))