import random

def guess_the_number():
    print("Welcome to Guess the Number!")
    print("Choose your difficulty: (1) easy, (2) medium, or (3) hard.")
    
    selected = False

    while not selected:
        difficulty = input("Difficulty: ").lower()
        if difficulty.isdigit():
            if difficulty == "1":
                max_number = 50
                attempts_allowed = 10
                selected = True
            elif difficulty == "2":
                max_number = 100
                attempts_allowed = 10
                selected = True
            elif difficulty == "3":
                max_number = 200
                attempts_allowed = 10
                selected = True
        else:
            print("Please choose a number between 1 and 3.")
            max_number = 100
            attempts_allowed = 10

    secret_number = random.randint(1, max_number)
    print(f"I'm thinking of a number between 1 and {max_number}. You have {attempts_allowed} tries!")

    for attempt in range(1, attempts_allowed + 1):
        guess = input(f"Attempt {attempt}: ")

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"You got it! The number was {secret_number}.")
            print(f"You guessed it in {attempt} tries!")
            return

    print(f"Out of tries! The number was {secret_number}.")


def main():
    guess_the_number()
    
if __name__ == "__main__":
    main()