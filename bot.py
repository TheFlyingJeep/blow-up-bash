import discord, json
from discord.ext import commands
inte = discord.Intents.all()
bot = commands.Bot(command_prefix=';', intents=inte)

@bot.event
async def on_ready():
    print("Starting up string!")
    
@bot.command(name="github", aliases=["git"])
async def github(ctx):
    await ctx.send("https://github.com/TheFlyingJeep/blow-up-bash")
    
if __name__ == "__main__":
    with open("secrets.json") as sec:
        data = json.load(sec)
        bot.run(data["token"])