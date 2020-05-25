"""
File: word_guess.py
-------------------
This is a word guessing game that prompts the player to guess one letter at a time
until either guessing the correct word or running out of guesses.
"""

import random

LEXICON_FILE = "Lexicon.txt"    # File to read word list from
INITIAL_GUESSES = 13            # Initial number of guesses player starts with


def play_game(secret_word):
    num_guesses = INITIAL_GUESSES
    dash_word = ''
    for i in range(len(secret_word)):
        dash_word += '-'
    print("The word now looks like this: " + dash_word)
    print("You have " + str(num_guesses) + " guesses left.")
    while num_guesses > 0: 
        guess = input("Type a single letter here, then press enter: ")
        guess = guess.strip()
        guess = guess.upper()
        if len(guess) > 1:
            print("Guess should only be a single character.")
            continue
        if guess in secret_word:
            if guess in dash_word:
                print("You already guessed this letter. Try again.")
            else:
                num_guesses -= 1
                print("That guess is correct.")
            dash_word = fill_dashes(secret_word, dash_word, guess)
            if dash_word == secret_word:
                print("Congratulations, the word is: " + secret_word)
                break
            if num_guesses == 0:
                print("Sorry, you lost. The secret word was: " + secret_word)
                break
        else:
            print("There are no " + guess + "'s in the word.")
            num_guesses -= 1
            if num_guesses == 0:
                print("Sorry, you lost. The secret word was: " + secret_word)
                break
        print("The word now looks like this: " + dash_word)
        print("You have " + str(num_guesses) + " guesses left.")

def fill_dashes(full_word, part_word, char):
    for i in range(len(full_word)):
        if full_word[i] == char:
            part_word = part_word[0:i] + char + part_word[i+1:]
    return part_word
    
def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game.  This function initially has a very small
    list of words that it can select from to make it easier for you
    to write and debug the main game playing program.  In Part II of
    writing this program, you will re-implement this function to
    select a word from a much larger list by reading a list of words
    from the file specified by the constant LEXICON_FILE.
    """

    word_list = []
    count = 0
    with open(LEXICON_FILE) as file:
        for line in file:
            line = line.strip()
            word_list += line.split()       
        for word in word_list:
            count += 1
        return word_list[random.randrange(count)]
    
def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    secret_word = get_word()
    play_game(secret_word)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
