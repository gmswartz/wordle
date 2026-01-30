import random

#list of alphabet
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#function to read through file and get a random word
def getrandomword():
    fileObj = open('/Users/graceswartz/Desktop/school/2022-2023/Fall 2022/CPSC230/GSwartz_Assignment6/words.txt')
    global words
    words = fileObj.readlines()
    #taking out extra space at the end of the word
    for index in range(len(words)):
        words[index] = words[index].replace('\n',"")

#function that creates random word (aka, 'wordle')
def readInput():
    random.choice(words)
    global wordle
    global word_1
    word_1 = len(words)
    wordle = words[random.randint(0, word_1 -1)].lower()

#function to print instructions for user
def printInstructions():
    print("Welcome to wordle. You have 6 tries to guess the randomly selected 5 letter word.")
    print("◼︎ means the letter you guessed is not in the word.")
    print("◻︎ means you guessed a correct letter, but it is not in the correct spot.")
    print("★ means you guessed the correct letter in the correct spot.")

#function to make sure guess is valid
def valid():
    global guess
    guess = input("Please guess a 5 letter word: ")
    #if guess is less/more than 5 letters
    if len(guess) != 5:
        print("You guess should contain 5 letters. Try again.")
        return False
    #if guess includes characters that are not letters
    if guess.isalpha() == False:
        print("Your input should only contain letters. Try again.")
        return False
    #if guess is not a valid word
    if guess not in words:
        print("This is not the correct words.")
        return False
    else:
        return True
    
#function for the game
#prints whether word is in correct place, incorrect place, or not in the word
#also prints out the remaining letters in a list
def success(guess):
    for x in range(len(guess)):
        if guess[x] in wordle:
            #if the letter is in the correct spot
            if wordle[x] == guess[x]:
                print("★", end = '\n')
                try:
                    list_index = alpha.index(guess[x])
                    alpha.pop(list_index)
                except ValueError:
                    continue
            #if letter is in the incorrect spot
            else:
                print("◻︎", end = '\n')
                try:
                    list_index = alpha.index(guess[x])
                    alpha.pop(list_index)
                except ValueError:
                    continue
        #if letter is not in the word      
        else:
            print("◼︎", end = '\n')
            try:
                list_index = alpha.index(guess[x])
                alpha.pop(list_index)
            except ValueError:
                continue
    if guess == wordle:
        print("You guessed the word! Congrats, you win!")
        return True

#calling functions
getrandomword()
readInput()
printInstructions()
print(wordle)

guessnum = 0
#loop to keep track of how many tries the user has used
while guessnum != 6:
    print("Your available letters are: \n", alpha)
    incorrect = valid()
    if incorrect == True:
        gameover = success(guess)
        guessnum = guessnum + 1
        if gameover == True:
            gameover = success(guess)
            break
#if user runs out of tries
if guessnum == 6:
    print("No more guesses, the word is: ", wordle)