import random
import sys

def getRandomWord():
    return random.choice(list(open("words.txt")))

def topBanner(): # for game visual
    print("\u001b[30m#------------------#")
    print(" SIX-LETTER  WORDLE ")

def deleteLine(): # used to clear line in output
    sys.stdout.write('\x1b[1A') #move up a line
    sys.stdout.write('\x1b[2K') #to clear line


def Game():
    while True: # loop for program
        finishedGame = False
        answer = getRandomWord() # get the answer
        correct = [False, False, False, False, False, False] # hold status
        turns = 0

        topBanner()
        if(turns == 6): # use max turns
            print("YOU LOSE")
            finishedGame = True
        
        while not finishedGame: # loop for in game
            guess = input("\u001b[30m")
            deleteLine()
            if guess.lower() == "quit": break
            if len(guess) != 6: continue
            

            outputline = "     "
            #compare the words
            for letter in range(0, len(guess)):
                if guess[letter] == answer[letter]: # if in right spot update status
                    correct[letter] = True
                    outputline += ("\u001b[32m"+ guess[letter] + " ") # print it green
                elif guess[letter] in answer:
                    outputline += ("\u001b[33m" + guess[letter] + " ") # print it yellow
                else:
                    outputline+= ("\u001b[30m" + guess[letter] + " ") # print it black

            print(outputline)
                
                

            turns += 1

            if all(correct): # all elements in correct evaluate to true
                finishedGame = True
                print("YOU WIN")

            



            



    


if __name__ == "__main__":
    Game()