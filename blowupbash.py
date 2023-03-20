import asyncio
import random
import time
from bubplayer import Player

with open("dictionary.txt", "r") as dict:
    dictionary = dict.read().lower().split("\n")

games = []


class BlowUpBash:
    def __init__(self):
        self.used_words = []
        self.play = True
        self.players = []
        self.joinable = True
        self.turn = 0

    async def game(self, ctx, client):
        welcome_msg = await ctx.send(
            "Welcome to Blow Up Bash! The game will start in 10s. Type \"join\" to join the game.")

        for i in range(10):
            time.sleep(1)
            await welcome_msg.edit(
                content=f"Welcome to Blow Up Bash! The game will start in {9 - i}s. Type \"join\" to join the game.")

        if len(self.players) < 2:
            await ctx.send("Not enough players. Canceling game...")
            await welcome_msg.edit(content="Game cancelled.")

        self.joinable = False
        await welcome_msg.edit(content="Game has started.")
        await ctx.send("Game is starting!")
        player_names = ""
        for i in self.players:
            print(i.getMsgObj().author.name)
            player_names += i.getMsgObj().author.name + ", "
        await ctx.send(f"Players in this game: {player_names}")

        def checkMsg(p):
            return p.channel == ctx.channel and p.author.id == self.players[self.turn].getMsgObj().author.id and prompt in p.content.lower() and p.content.lower() in dictionary and p.content not in self.used_words

        while self.play:
            prompt = await generatePrompt(ctx)
            await ctx.send(f"{self.players[self.turn].getMsgObj().author.mention}'s turn! Your prompt is: {prompt}")
            try:
                msg = await client.wait_for("message", timeout=random.randrange(1, 20), check=checkMsg)
                await ctx.send(f"{msg.content.lower()} is a valid guess")
                self.used_words.append(msg.content)
                print(self.used_words)
            except asyncio.TimeoutError:
                await ctx.send("Time over!")
                self.players[self.turn].lifeLoss()

            current_turn = self.turn
            next_turn = self.turn + 1
            if next_turn < len(self.players)-1:
                if self.players[next_turn].getLifeStatus():
                    print("e")
            else:
                self.turn = 0

        await ctx.send("Game over!")


async def generatePrompt(ctx):
    possible_prompts = ["con", "hea", "car", "ivi", "ump", "ive", "es", "ic", "ks", "tr", "to", "bil", "sts", "tt",
                        "wr", "omi", "ti", "ap", "rk", "en", "op", "ial", "omp", "arr", "sm", "ie", "on", "nis", "ron",
                        "fl", "ns", "lo", "ns", "no", "nds", "tr", "an", "li", "re", "ut", "tim", "chi", "an", "oth",
                        "pe", "ent", "amp", "is", "al", "mo", "er", "tio", "fi", "ilo", "nes", "ch", "nt", "in", "gge",
                        "er", "sti", "bl", "ha", "din", "un", "le", "in", "sms", "ba", "bu", "lu", "ra", "ina", "ni",
                        "io", "ari", "ret", "go", "con", "ion", "er", "he", "no", "om", "der", "ch", "pe", "al", "ant",
                        "is", "ing", "om", "olo", "per", "ula", "nch", "ss", "tha", "esi", "ano", "hob", "es", "mat",
                        "al", "te", "ic", "es", "ing", "nst", "of", "rh", "su", "dr", "re", "lo", "al", "po", "ho",
                        "yp", "is", "eat", "na", "er", "erg", "co", "pp", "ea", "no", "rma", "io", "her", "st", "war",
                        "nc", "lay", "fa", "ize", "ba", "rip", "ze", "og", "his", "oli", "mat", "ch", "ism", "rco",
                        "az", "nce", "oun", "ar", "ic", "ph", "hi", "dar", "qui", "end", "pr", "ata", "api", "ss", "sh",
                        "iv", "utt", "ed", "ct", "rc", "iz", "ram", "at", "pe", "ip", "ti", "ut", "els", "ls", "ck",
                        "mis", "der", "mi", "nt", "re", "im", "bal", "uli", "dio", "ac", "ali"]
    return random.choice(possible_prompts)


async def addPlayers(msg):
    global games
    for i in games:
        if i.joinable and msg.author not in i.players:
            player = Player(msg)
            i.players.append(player)
            break
