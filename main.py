import random

def compareNumber(secretNumber, userInput):
    if secretNumber == userInput:
        print("You guessed right!")
        return True
    else:
        if userInput < secretNumber:
            print("Number should be higher, try again!")
        elif userInput > secretNumber:
            print("Number should be lower, try again!")
        return False
    
def userGuess():
    return int(input("What is the secret number? "))

def computerGuess():
    randomNumber = random.randint(1, 100)
    print("Computer guessed:", randomNumber)
    return randomNumber

def main():
    secretNumber = random.randint(1, 100)

    while True:
        userInput = userGuess()
        if compareNumber(secretNumber, userInput) == True:
            break

        computerInput = computerGuess()
        if compareNumber(secretNumber, computerInput) == True:
            break

main()