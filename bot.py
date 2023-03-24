import discord, json
from discord.ext import commands
import trivia as triv
import vroomskirt as vs
import anagrams as ana
import wordle as word
import blowupbash as bub
inte = discord.Intents.all()
bot = commands.Bot(command_prefix=';', intents=inte)

@bot.event
async def on_ready():
    print("Starting up string!")

@bot.event
async def on_message(msg):
    await ana.checkMsg(msg)
    if msg.content.lower() == "join":
        await bub.addPlayers(msg)
    await bot.process_commands(msg)

@bot.event
async def on_raw_reaction_add(payload):
    if not payload.member.bot  and str(payload.emoji) == "✅" and payload.message_id in triv.trivia_games:
        await triv.tryJoin(payload)
    elif not payload.member.bot  and str(payload.emoji) == "✅" and payload.message_id in vs.vsgames:
        await vs.tryJoin(payload)

@bot.command(name="trivia")
async def trivia(ctx):
    await ctx.send("Just answer trivia questions! First to five points wins!")
    await triv.startGame(ctx, bot)

@bot.command(name="vroomskirt", aliases=["vs"])
async def vroomskirt(ctx):
    await vs.startGame(ctx, bot)

@bot.command(nmae="pydle")
async def pydle(ctx):
    await word.pydle(ctx, bot)

@bot.command(name="blowupbash", aliases=["bub"])
async def blowupbash(ctx):
    bubgame = bub.BlowUpBash(ctx)
    bub.games.append(bubgame)
    await bubgame.game(ctx, bot)
    
if __name__ == "__main__":
    with open("secrets.json") as sec:
        data = json.load(sec)
        bot.run(data["token"])