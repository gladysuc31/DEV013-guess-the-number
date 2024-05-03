"""Main"""
import random

def compare_number(secret_number, user_input):
    """Compare guess to the correct number"""
    if secret_number == user_input:
        return True, "You guessed right!"
    if user_input < secret_number:
        return False, "Number should be higher, try again!"
    if user_input > secret_number:
        return False, "Number should be lower, try again!"

def user_guess():
    """Get the user´s guess"""
    while True:
        try:
            return int(input("What is the secret number? "))
        except ValueError:
            print("Please enter a valid number.")

def computer_guess():
    """Get computer´s guess"""
    random_number = random.randint(1, 100)
    print("Computer guessed:", random_number)
    return random_number


def store_attempts(user_attempts, attempt):
    """Function to store the user´s guesses"""
    user_attempts.append(attempt)


def main():
    """Game implementation"""
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

if __name__=="__main__":
    main()
#End-of-file (EOF)