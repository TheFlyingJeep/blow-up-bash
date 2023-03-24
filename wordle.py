import random
import asyncio

with open('valid_words.txt') as f:
    data = f.read()

with open ("pydle_words.txt", "r") as file: 
    words = file.read()

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
green_letters = ['<:a_green:1080896945444356166>', '<:b_green:1080896994337362060>', '<:c_green:1080896995264303144>', '<:d_green:1080896997386616862>', '<:e_green:1080896998284214332>', '<:f_green:1080896999563464785>', '<:g_green:1080897048947196016>', '<:h_green:1080897049974800465>', '<:i_green:1080897051413454942>', '<:j_green:1080897053015679066>', '<:k_green:1080897054219440189>', '<:l_green:1080897135991607327>', '<:m_green:1080897137442836491>', '<:n_green:1080897138692722778>', '<:o_green:1080897139841978398>', '<:p_green:1080897140882153662>', '<:q_green:1080897167385968750>', '<:r_green:1080897169583771648>', '<:s_green:1080897172108759101>', '<:t_green:1080898104150196234>', '<:u_green:1080897174516285440>', '<:v_green:1080897176298864650>', '<:w_green:1080897210612457584>', '<:x_green:1080897213422637076>', '<:y_green:1080897214265704496>', '<:z_green:1080897215725310102>']
yellow_letters = ['<:a_yellow:1080889822756999301>', '<:b_yellow:1080889965824725102>', '<:c_yellow:1080889967343046779>', '<:d_yellow:1080889968446160986>', '<:e_yellow:1080889969259851938>', '<:f_yellow:1080889970706882670>', '<:g_yellow:1080889972795645992>', '<:h_yellow:1080889973789704202>', '<:i_yellow:1080889975568093245>', '<:j_yellow:1080889976746672321>', '<:k_yellow:1080890280225546310>', '<:l_yellow:1080890111375462400>', '<:m_yellow:1080890113019629658>', '<:n_yellow:1080890113854292061>', '<:o_yellow:1080890115183878175>', '<:p_yellow:1080890116429586502>', '<:q_yellow:1080890117780144201>', '<:r_yellow:1080890118572867716>', '<:s_yellow:1080890175913218099>', '<:t_yellow:1080890177536397352>', '<:u_yellow:1080890178631106662>', '<:v_yellow:1080890181051228310>', '<:w_yellow:1080890182380814417>', '<:x_yellow:1080890184008220805>', '<:y_yellow:1080890207638921277>', '<:z_yellow:1080890208981090427>']
gray_letters = ['<:a_gray:1079602623348478053>', '<:b_gray:1079603340721279016>', '<:c_gray:1079603798751838299>', '<:d_gray:1079604022190800907>', '<:e_gray:1079604218459082843>', '<:f_gray:1079606364982231114>', '<:g_gray:1079606608625160222>', '<:h_gray:1079607016709959710>', '<:i_gray:1079608947201294366>', '<:j_gray:1079608948849643560>', '<:k_gray:1079608949810155650>', '<:l_gray:1079608950443495466>', '<:m_gray:1079608952268017804>', '<:n_gray:1079608953886998578>', '<:o_gray:1079608955250147360>', '<:p_gray:1079610657147736175>', '<:q_gray:1079610659756593254>', '<:r_gray:1079610660448641066>', '<:s_gray:1079610780359606282>', '<:t_gray:1079610781924077649>', '<:u_gray:1079610783165587518>', '<:v_gray:1079610784985927791>', '<:w_gray:1079610786713964544>', '<:x_gray:1079610788026794005>', '<:y_gray:1079610789293473863>', '<:z_gray:1079610791088627732>']
corr_letters = []
def valid_word(guess):
    if guess in data:
        return True
    else:
        return False



def display_guess(guess, answer):
    guess = guess.content

    print(guess)
    
    guess_msg = ""
    guess_msg_array = [*guess]
    answer_array = [*answer]
    letters_left = [*answer]
    print (guess_msg_array)
    print (answer_array)
    colorArr = []

    i = 0

    for char, g in zip(answer,guess):
        print(guess_msg_array[i])

        ind = letters.index(g)

        if g in answer and g in char:
            # colorArr.append("green")
            guess_msg += green_letters[ind]
        elif g in answer:
            # colorArr.append("yellow")
            guess_msg += yellow_letters[ind]
        else: 
            # colorArr.append("gray")
            guess_msg += gray_letters[ind]

    return guess_msg


        
            
        

        # if (answer_array[i] == guess_msg_array[i]) and (guess in char) :
        #     guess_msg += green_letters[letters.index(guess[i])]
        #     corr_letters.append(guess_msg_array[i])
        # elif guess_msg_array[i] in answer_array:
        #     guess_msg += yellow_letters[letters.index(guess[i])]
        # else:
        #     guess_msg += gray_letters[letters.index(guess[i])]

        # i = i + 1
        # if guess_msg_array[i] == answer_array[i]:
        #     guess_msg += green_letters[letters.index(guess[i])]
        #     corr_letters.append(guess_msg_array[i])
        # elif not guess_msg_array[i] in answer_array:
        #     guess_msg += gray_letters[letters.index(guess[i])]
        # else:
        #     if not guess_msg_array[i] in corr_letters:
        #         guess_msg += yellow_letters[letters.index(guess[i])]
        #     else:
        #         guess_msg += gray_letters[letters.index(guess[i])]




        # if all else fails use this one lauren :) 

        # if (guess_msg_array[i] in answer_array) == False:
        #     guess_msg += gray_letters[letters.index(guess[i])]
        # elif guess_msg_array.index(guess[i]) == answer_array.index(guess[i]):
        #     guess_msg += green_letters[letters.index(guess[i])]
        #     if guess[i] in letters_left: 
        #         letters_left.index(guess_msg_array[i])
        # else:
        #     if guess
        #     guess_msg += yellow_letters[letters.index(guess[i])]


        # #if guess_msg_array[i] in answer:
        # if guess[i] in answer_array and guess_msg_array.index(guess[i]) == answer_array.index(guess[i]):
        #     guess_msg += green_letters[letters.index(guess[i])]
        #     if guess[i] in corr_letters == False: 
        #         corr_letters.append(guess_msg_array[i])
        # elif guess_msg_array[i] in answer == False:
        #         guess_msg += gray_letters[letters.index(guess[i])]
        # else:
        #     # if guess_msg_array[i] in corr_letters:
        #         guess_msg += yellow_letters[letters.index(guess[i])]
        #     # else:
        #         # guess_msg += gray_letters[letters.index(guess[i])]

async def pydle(ctx, client):

    def valid_guess(p):
         # input checking yay!
        p.content = p.content.lower()
        if p.content.isalpha() == False:
            return False
        elif len(p.content) < 5:
            return False
        elif len(p.content) > 5:
            return False
        elif valid_word(p.content) == False:
            return False
        else:
            return True


    async with ctx.typing():
        # intro + selects a word
        await ctx.send("Welcome to Pydle: a programming-themed word game!")
        await ctx.send("Welcome to Pydle, a coding-theme Wordle!\nEnter in a valid, 5 letter guess below.\n🟩 : Letter is correct AND in the right place\n🟨 : Letter is in the word BUT not in the right place (in development) \n⬜ : Letter is NOT in the word \nYou have 6 guesses, good luck!")
        chosen_word = random.choice(words.splitlines())
        # await ctx.send(chosen_word)

        guess_count = 1
        while guess_count < 6:
            await ctx.send("Guess " + str(guess_count) + " out of 6")
            await ctx.send("Please type in a 5 letter guess below: ")

        # user response
            try:
                guess = await client.wait_for("message",timeout=30, check=valid_guess)
                await ctx.send("Valid guess!")

                str(guess)

                # print(guess)
                print(chosen_word)
                await ctx.send(display_guess(guess, chosen_word))
                guess_count = guess_count + 1 

                # when done
                if guess.content.lower() == chosen_word.lower():
                    if guess_count == 1:
                        await ctx.send("Lucky guess!") 
                        break
                    elif guess_count == 2:
                        await ctx.send("Well done!") 
                        break
                    elif guess_count == 3:
                        await ctx.send("Amazing!") 
                        break
                    elif guess_count == 4:
                        await ctx.send("Great job!") 
                        break
                    elif guess_count == 5:
                        await ctx.send("Cool!") 
                        break
                    elif guess_count == 6:
                        await ctx.send("Close one!") 
                        break
                elif guess_count > 6:
                    await ctx.send("The word was: " + chosen_word)
                    break

            except asyncio.TimeoutError:
                await ctx.send("Oops, this Pydle has timed out! Start a new game with `racc pydle`")
                break