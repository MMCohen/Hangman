import random
from hangman_words import WORDS

MAX_TRIES = 8
lst_of_words = WORDS

def get_random_word() -> str:
    """
    gets a random word from the list
    :return: word as str
    """
    return random.choice(lst_of_words)


def hide_the_word(char_lst: str) -> list[str]:
    """
    converts the letters into "_".
    ex. "ex" -> ['_', '_']
    :param char_lst:
    :return: list[str]
    """
    return ["_" for _ in char_lst]


# def convert_word_to_lst(word: str) -> list[str]:
#     return list(word)


def get_user_guess() -> str:
    """
    asks the user for a letter.
    before returning the letter, validate that it is a letter and only one letter with validate_guess func.
    :return: one str letter lowercase
    """
    while True:
        user_guess = input("Please enter a letter: ")
        if validate_guess(user_guess):
            return user_guess.lower()


def validate_guess(user_guess: str) -> bool:
    """
    checks that the user entered a letter and only one letter.
    :param user_guess:
    :return: True / False
    """
    return user_guess.isalpha() and len(user_guess) == 1


def print_the_word(hidden_word: list) -> None:
    """
    prints the word into the terminal. transform the word from 'a','b','c' -> abc
    :param hidden_word:
    :return: None
    """
    print(f"your hangman word is: {" ".join(hidden_word)}")
    return None


def reveal_correct_letters(random_word, hidden_word, user_guess) -> list[str]:
    """
    reveals the correct letters
    ex: if the word is ['h','e','l','l','o'] looks like _____ and the player guess 'l' the function will reveal __ll_
    :param random_word:
    :param hidden_word:
    :param user_guess:
    :return: list
    """
    for idx, letter in enumerate(random_word):
        if user_guess == letter:
            hidden_word[idx] = letter
    return hidden_word


def is_won(random_word, hidden_word) -> bool:
    """
    checks if the player finish to guess the word
    :param random_word:
    :param hidden_word:
    :return: True / False
    """
    return not "_" in hidden_word


def main():
    random_word = get_random_word()
    hidden_word = hide_the_word(random_word)

    won_the_game = False
    tries_left = MAX_TRIES
    letters_guessed_by_the_user = set()

    while tries_left > 0 and not won_the_game:
        print(random_word)
        print(f"the letters you already enter: {letters_guessed_by_the_user}") if letters_guessed_by_the_user else None
        print(f"tries left: {tries_left}")
        print_the_word(hidden_word)
        user_guess = get_user_guess()
        letters_guessed_by_the_user.add(user_guess)

        if user_guess in random_word:
            hidden_word = reveal_correct_letters(random_word, hidden_word, user_guess)
            won_the_game = is_won(random_word, hidden_word)
        else:
            tries_left -= 1

    if won_the_game:
        print("well done!")
    else:
        print(f"the word was: {random_word}")
        print("next time...")


if __name__ == '__main__':
    main()