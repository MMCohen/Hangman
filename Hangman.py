import random

MAX_TRIES = 8
lst_of_words = []
letters_guessed_by_the_user = []


def get_random_word() -> str:
    """
    gets a random word from the list
    :return: word as str
    """
    return random.choice(lst_of_words)


def hide_the_word(char_lst: list[str]) -> list[str]:
    """
    converts the letters into "_".
    ex. ['e', 'x'] -> ['_', '_']
    :param char_lst:
    :return: list[str]
    """
    return ["_" for char in char_lst]


def convert_word_to_lst(word: str) -> list[str]:
    return list(word)


def get_user_guess() -> str:
    """
    asks the user for a letter.
    before returning the letter, validate that it is a letter and only one letter with validate_guess func.
    :return: str
    """
    while True:
        user_guess = input("Please enter a letter: ")
        if validate_guess(user_guess):
            return user_guess


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
    print(f"your hangman is: {"".join(hidden_word)}")
    return None


def main():
    pass


if __name__ == '__main__':
    main()