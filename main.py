import random

#Compare guess to the correct number
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
    
#Get the user´s guess
def userGuess():
    return int(input("What is the secret number? "))


#Get computer´s guess
def computerGuess():
    randomNumber = random.randint(1, 100)
    print("Computer guessed:", randomNumber)
    return randomNumber

#Function to store the user´s guesses
def storeAttempts(userAttempts, attempt):
    userAttempts.append(attempt)

#Game implementation
def main():
    secretNumber = random.randint(1, 100)
    print(secretNumber)
    userAttempts = []
    computerAttempts = []

    while True:
        userInput = userGuess()
        storeAttempts(userAttempts, userInput)
        
        
        if compareNumber(secretNumber, userInput) == True:
            print(userAttempts)
            break

        computerInput = computerGuess()
        storeAttempts(computerAttempts, computerInput)
        if compareNumber(secretNumber, computerInput) == True:
            print(computerAttempts)
            break

main()