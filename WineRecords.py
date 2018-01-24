WineRecords = {
    "ID": "Wine", 
}
def main(ctx):
    try:
        WineRecords[str(ctx.author.id)] += 1
    except KeyError:
        WineRecords[str(ctx.author.id)] = 1
    return f"*{ctx.author.mention} has been given {WineRecords[str(ctx.author.id)]} glasses of :wine_glass:!*"
