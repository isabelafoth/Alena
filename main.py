import discord
from discord.ext import commands, tasks
import os

bot = commands.Bot(command_prefix="!", case_insensitive=True, intents=discord.Intents().all())


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online)
    print(f"Logged in as {bot.user}.")

@bot.command(aliases=["p"])
async def ping(ctx):
    ping = round(bot.latency*1000)
    if ping >= 1000:
        react = "<///3"
    elif ping >= 750:
        react = "<//3"
    elif ping >= 500:
        react = "</3"
    elif ping >= 100:
        react = "<3"
    elif ping >= 50:
        react = "<33"
    else:
        react = "<333"
    await ctx.send(f"*{react}*   ||{ping}ms||")


@bot.command(aliases=["rl", "r"])
async def reload(ctx, cog=None):
    await ctx.send("oki!!")
    print(f"Attempting to unload \"{cog}\"...")
    try:
        if cog:
            bot.unload_extension(cog)
        else:  # Empty = all
            for filename in os.listdir():
                if filename.endswith(".py") and filename != os.path.basename(__file__):
                    print(f"Attempting to unload \"{filename[:-3]}\"...")
                    bot.unload_extension(filename[:-3])
                    print("Successful!")
    except (commands.ExtensionNotFound, commands.NotLoaded) as e:
        if isinstance(e, commands.ExtensionNotFound):
            await ctx.send(f"cog `{cog}` was not found while unloading!! :(")
            return
        else:
            pass  # It's not loaded yet so we'll just skip
        print(e)
    print("Successful!")

    print(f"Attempting to load \"{cog}\"...")
    try:
        if cog:
            bot.load_extension(cog)
        else:  # Empty = all
            for filename in os.listdir():
                if filename.endswith(".py") and filename != os.path.basename(__file__):
                    print(f"Attempting to load \"{filename[:-3]}\"...")
                    bot.load_extension(filename[:-3])
                    print("Successful!")
    except (commands.ExtensionNotFound, commands.NoEntryPointError, commands.ExtensionFailed) as e:
        if isinstance(e, commands.ExtensionNotFound):
            await ctx.send(f"cog `{cog}` was not found while loading!! :(")
        else:
            await ctx.send(f"uh.. not sure,, something confusing happened while loading **{cog}** :(\n`{e}`")
        print(e)
        return
    print("Successful!")

    await ctx.send("done! ^-^")


for filename in os.listdir():
    if filename.endswith(".py") and filename != os.path.basename(__file__):
        print(f"Loading {filename}...")
        bot.load_extension(filename[:-3])
        print("Loaded! ^-^")


bot.run("ID")
