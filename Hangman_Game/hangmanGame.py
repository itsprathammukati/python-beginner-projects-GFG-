import random
from lists import wordList

# if user entered guess is one character and alphabet but already guessed
word = random.choice(wordList)
wordInListFormat = list(correctWord)

guessList = ['_'] * len(wordInListFormat)

maxAttempts = 6

while maxAttempts > 0:

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
                        print(f"You have {maxAttempts}/12 maxAttempts remaining.")
                else:
                    print("Uhuhh your guess was incorrect.")
                    maxAttempts -= 1
                    print(f"You have {maxAttempts}/12 maxAttempts remaining.")

    if guessList == word:
        print(f"WOHOOO!!! YOU WIN. {correctWord.upper()} is the correct word.")
        break
    
if maxAttempts == 0:
    print(f"You lose. {correctWord.upper()} was the correct word.")
