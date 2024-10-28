from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0

def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("That is too high...")
        return turns - 1
    elif user_guess < actual_answer:
        print("That is too low...")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")


def set_difficulty():
    level = input("Choose a difficulty: Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100...")
    answer = randint(a=1, b=100)
    # print(f"Psst, the correct answer is {answer}")

    turns = set_difficulty()


    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Please make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You ran out of guesses and thereby, lose...:(")
            return
        elif guess != answer:
            print("Guess again!")

game()