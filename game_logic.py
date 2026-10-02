import random
from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def display_game_state(mistakes, secret_word, guessed_letters):
    print(STAGES[mistakes])
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_"
    print("Word: ", display_word)
    print("\n")

def play_game():
    mistakes = 0
    secret_word = get_random_word()
    guessed_letters = []

    print("Welcome to Snowman Meltdown!")
    display_game_state(mistakes, secret_word, guessed_letters)

    while True:
        guess = input("Guess a letter: ").lower()
        print("You guessed:", guess)
        if guess in secret_word:
            guessed_letters.append(guess)
            display_game_state(mistakes, secret_word, guessed_letters)
        elif guess not in secret_word:
            mistakes += 1
            print(mistakes)
            display_game_state(mistakes, secret_word, guessed_letters)

        if all(letter in guessed_letters for letter in secret_word):
            print("Congratulations! You saved the snowman and guessed the word!")
            break
        if mistakes == 3:
            print("Too many mistakes")
            break
        