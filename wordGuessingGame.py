import random
from lists import wordList

# if user entered guess is one character and alphabet but already guessed
correctWord = random.choice(wordList)
word = list(correctWord)

guessList = ['_'] * len(word)

turns = 12

while turns > 0:

    guess = input("Enter your guess: ").lower()

    if len(guess) != 1:
        print("Enter only one letter.")
    else:
        if not guess.isalpha():
            print("Enter an alphabet.")
        else:
            if guess in guessList:
                print("Letter already in list.")
            else:
                if guess in word:
                    for i in range(len(word)):
                        if guess == word[i]:
                            guessList[i] = word[i]
                    print(guessList)
                    if guessList != word:
                        print(f"You have {turns}/12 turns remaining.")
                else:
                    print("Uhuhh your guess was incorrect.")
                    turns -= 1
                    print(f"You have {turns}/12 turns remaining.")

    if guessList == word:
        print(f"WOHOOO!!! YOU WIN. {correctWord.upper()} is the correct word.")
        break
    
if turns == 0:
    print(f"You lose. {correctWord.upper()} was the correct word.")
