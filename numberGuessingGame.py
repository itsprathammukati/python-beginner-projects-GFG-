import random # Imported random module.

number = random.randint(1, 100)
attempts = 7

while True:

    print(f"Attempt remaining {attempts}/7")
    userInput = int(input("Enter your guess: "))    

    if userInput > 100 or userInput < 1:
        print("Your guess is out of range")
    else:
        attempts -= 1
        if userInput == number:
            print("You Win!!!")
            break
        elif userInput > number:
            print("Your guess is too high")
        elif userInput < number:
            print("Your guess is too low")

    if attempts == 0:
        print(f"The number was {number}. You are out of lives!")
        break