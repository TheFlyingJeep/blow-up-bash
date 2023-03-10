#anagrams
import random, time, discord, json
from discord.ext import commands
inte = discord.Intents.all()
bot = commands.Bot(command_prefix=';', intents=inte)
@bot.event
async def on_ready():
  print("Starting up string!")


file1 = open('dict.txt', 'r')
print("");
lines = file1.read().splitlines()
print("");
alphabet = "aeioulmnftl"
letters = []
used = []
totalPoints = 0; 
countdown = 0; 

def countdown(t):
    countdown = t
    while countdown:
        mins, secs = divmod(countdown, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        countdown -= 1

def checkWord(word):
  global lines, letters, used
  usedLetters = []
  if used.__contains__(word):
    return False
  if not lines.__contains__(word):
    return False
    
  for x in word:
    if not letters.__contains__(x) or usedLetters.__contains__(x):
     return False; 
    else:
      usedLetters.append(x)
  return True

  





x = 0
while x < 6:
    rand = random.randint(0,10)
    if letters.__contains__(alphabet[rand]):
       pass
    else:
        letters.append(alphabet[rand])
        x=x+1

print("Welcome to Anagrams. Make as many words as you can with the given letters!")
print("Your letters are: ", letters)
countdown(int(10))
game = True; 
while game == True:
  word = input("Guess: ")
  word = word.lower()
  validWord = True
  
  if checkWord(word):
    used.append(word)
    totalPoints += len(word) * 100
    print(len(word) * 100, "points")
  else:
    while not checkWord(word):
      word = input("Invalid word. Try again: ")
    used.append(word);
    totalPoints += len(word) * 100
    print(len(word) * 100, "points")
  
  
    

