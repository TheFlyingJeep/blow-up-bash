import random, time
letters = []
alphabet = "aeioulmntls"
used = []
totalPoints = 0
player = None
isPlaying = False
file1 = open('dictionary.txt', 'r')
lines = file1.read().splitlines()
timeMsg = ""

async def checkMsg(msg):
  global totalPoints, letters, alphabet, used, lines
  if isPlaying:
    if msg.author == player:
      if await checkWord(msg):
       used.append(msg.content)
       totalPoints += len(msg.content) * 100
       points = str(len(msg.content) * 100) + " points!\n" + str(timeMsg.content) + " Your letters are: "
       await msg.channel.send(points)
       await msg.channel.send(letters)
      else:
        await msg.channel.send(timeMsg.content)
        await msg.channel.send("Invalid word. \nYour Letters are: ")
        await msg.channel.send(letters)

async def anagrams(ctx):
  global letters, alphabet, totalPoints, lines, used, isPlaying, player
  await ctx.send("test")
  await createLetters()
  await ctx.send("Welcome to Anagrams. Make as many words as you can with the given letters! \nYour letters are: ")
  await ctx.send(letters)
  isPlaying = True
  player = ctx.author
  await gameLoop(ctx)
  



   


async def gameLoop(ctx):
        global isPlaying, player, totalPoints, letters, used,timeMsg
        timeMsg = await ctx.send("Time: ")
        for i in range(60):
            time.sleep(1)
            timeMsg.content = "You have " + str(60-i) + " seconds left!"
          
            await timeMsg.edit(content=f"{ctx.author.mention} You have {60-i} seconds left!")
        await timeMsg.edit(content="Game over!")
        await ctx.send("Game over. You scored: " + str(totalPoints) + " points!")
        isPlaying = False
        player = None
        totalPoints = 0
        letters = []
        used = []
  
        


async def checkWord(msg):
  global lines, letters, used
  word = msg.content
  usedLetters = []
  if used.__contains__(word):
    return False
  if not lines.__contains__(word):
    return False
    
  for x in word:
    if not letters.__contains__(x) or usedLetters.__contains__(x):
     return False
    else:
      usedLetters.append(x)
  return True

async def createLetters():
  global alphabet, letters
  x = 0
  while x < 6:
     rand = random.randint(0,10)
     if letters.__contains__(alphabet[rand]):
        pass
     else:
         letters.append(alphabet[rand])
         x=x+1