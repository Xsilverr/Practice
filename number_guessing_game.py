import random


def guess():
    return (random.randint(1, 100))


def compare(computer_guessed_number, player_guessed_number, lives):
    if computer_guessed_number > player_guessed_number:
        print("Too low.")
        return lives - 1
    elif computer_guessed_number < player_guessed_number:
        print("Too high.")
        return lives - 1
    else:
        print(f"You got it! The answer was {computer_guessed_number}")


# the main game loop
# Welcome message
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Choosing the difficulty level
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == 'easy':
    lives = 10
else:
    lives = 5

# computer to guess a number
computer_guess = guess()
print(computer_guess)
# player to input guessed number

# if condition to inform the player if the number is lower or higher
player_guess = 0
while computer_guess != player_guess:
    print(f"You have {lives} attempts remaining to guess the number.")
    player_guess = int(input("Make a guess: "))
    lives = compare(computer_guessed_number=computer_guess, player_guessed_number=player_guess, lives=lives)
    if lives == 0:
        print("You've run out of guessess, you lose.")
        break
    elif player_guess != computer_guess:
        print("Guess again.")
