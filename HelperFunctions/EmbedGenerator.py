########################################################################################################################
#                                                 HELPER FUNCTIONS                                                     #
########################################################################################################################
""" Contains Functions that may assist in certain tasks."""

import discord


def EmbGen(title=None, description=None, footer=None, author=None, *fields, color=0xff8040):
    """This Function will be used to generate embeds on the go, For any command to use if needed."""
    url = r"https://cdn.discordapp.com/app-icons/369099294579359744/85818996c0ccfd1030b096f4c3dcf23f.png"
    embed = discord.Embed(title=title if not None else "",
                          description=description if not None else "",
                          color=color)

    if author is not None:
        embed.set_author(
            name=author,
            icon_url=url
        )

    if fields is not None:
        for name, value in fields:
            embed.add_field(name=name, value=value, inline=True)

    if footer is not None:
        embed.set_footer(text=footer)

    return embed
