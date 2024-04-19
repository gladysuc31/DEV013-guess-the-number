import random

secretNumber = random.randint(1, 100)

while True:
    userInput = int(input("What is the secret number? "))
    
    if userInput == secretNumber:
        print("You guessed right!")
        break
    else:
        if userInput < secretNumber:
            print("Number should be higher, try again!")
        elif userInput > secretNumber:
            print("Number should be lower, try again!")