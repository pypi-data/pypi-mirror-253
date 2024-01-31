"""Hangman in the terminal."""

from hungmen import WORKING_DIRECTORY
from hungmen.hangman import Hangman, WordBank

BANK = WordBank(WORKING_DIRECTORY / "banks" / "whoopi.json")


def main() -> None:
    """Wanna hang, man?"""
    print("Let's play Hangman!")
    game = Hangman(BANK)
    while game.status == "in-progress":
        game.print()
        guess = input("Guess a letter or word: ")
        game.guess(guess)
    play_again = input(
        f"You {game.status}! The word was '{game.secret_word}'. Play again? [Y/N]: "
    )
    if "Y" in play_again.upper():
        main()
    else:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
