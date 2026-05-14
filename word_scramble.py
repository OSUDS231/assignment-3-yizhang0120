import random

# ----------------------------------------------------
# PROVIDED HELPER FUNCTIONS (DO NOT MODIFY)
# ----------------------------------------------------

def load_words(filename="words.txt"):
    """
    Loads the word list from a file and returns a list of words.
    Each word is assumed to be in lowercase.
    """
    print("Loading word list from file...")
    with open(filename, 'r') as f:
        wordlist = f.read().split()
    print(f"{len(wordlist)} words loaded")
    return wordlist

def choose_word(wordlist):
    """
    wordlist: list of strings
    returns: string, a randomly chosen word from the list
    """
    return random.choice(wordlist)

def scramble_word(secret_word):
    """
    Scrambles the letters of the given secret word and prints the scrambled version.
    Does not return anything.
    """
    letters = list(secret_word)
    random.shuffle(letters)
    scrambled = ''.join(letters)
    print(f"Scrambled word: {scrambled}")

# ----------------------------------------------------
# FUNCTIONS TO IMPLEMENT
# ----------------------------------------------------

# Task 1.1 
def input_check(secret_word):
    while True:
        guess = input("Your guess: ")
        guess_cleaned = ""

        for c in guess:
            if c.isalpha():
                guess_cleaned = guess_cleaned + c.lower()

        if sorted(guess_cleaned) == sorted(secret_word):
            return guess_cleaned
        else:
            print("Invalid input. Please use only the letters from the secret word.")

# Task 1.2
def has_player_won(secret_word, user_guess):
    if secret_word == user_guess:
        return True
    else:
        return False

# Task 1.3 
def get_word_progress(secret_word, user_guess):
    progress = ""

    for i in range(len(secret_word)):
        if secret_word[i] == user_guess[i]:
            progress = progress + secret_word[i]
        else:
            progress = progress + "*"

    return progress

# Task 2.1, 2.2 
def word_scramble():
    word_list = load_words()
    secret_word = choose_word(word_list)
    attempts = 5

    print("Welcome to Word Scramble!")
    scramble_word(secret_word)
    print("You have 5 attempts to guess the original word.")

    while attempts > 0:
        print()
        user_guess = input_check(secret_word)

        if has_player_won(secret_word, user_guess):
            print(f"Congratulations! You guessed the word: {secret_word}")
            return
        else:
            attempts = attempts - 1
            progress = get_word_progress(secret_word, user_guess)
            print(f"Incorrect. Progress: {progress}")
            print(f"Attempts left: {attempts}")

    print(f"Sorry, you ran out of guesses. The word was {secret_word}.")

if __name__ == "__main__":
    word_scramble()
