import random

#Compare guess to the correct number
def compare_number(secret_number, user_input):
    if secret_number == user_input:
        return True, "You guessed right!"
    else:
        if user_input < secret_number:
            return False, "Number should be higher, try again!"
        elif user_input > secret_number:
            return False, "Number should be lower, try again!"
    
#Get the user´s guess
def user_guess():
    while True:
        try:
            return int(input("What is the secret number? "))
        except ValueError:
            print("Please enter a valid number.")


#Get computer´s guess
def computer_guess():
    random_number = random.randint(1, 100)
    print("Computer guessed:", random_number)
    return random_number

#Function to store the user´s guesses
def store_attempts(user_attempts, attempt):
    user_attempts.append(attempt)

#Game implementation
def main():
    secret_number = random.randint(1, 100)
    print(secret_number)
    user_attempts = []
    computer_attempts = []

    while True:
        user_input = user_guess()
        store_attempts(user_attempts, user_input)
        
        result, message = compare_number(secret_number, user_input)
        print(message)
        
        if result:
            print("User attempts: " + str(user_attempts))
            break

        computer_input = computer_guess()
        store_attempts(computer_attempts, computer_input)
        
        result, message = compare_number(secret_number, computer_input)
        print(message)
        
        if result:
            print("The computer attempts: " + str(computer_attempts))
            break

main()