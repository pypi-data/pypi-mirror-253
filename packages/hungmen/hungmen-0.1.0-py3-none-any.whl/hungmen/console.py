"""Hangman in the terminal."""

from hangman.hangman import Hangman


def main() -> None:
    """Wanna hang, man?"""
    print("Let's play Hangman!")
    game = Hangman()
    while game.status == "in-progress":
        game.print()
        guess = input("Guess a letter or word: ")
        game.guess(guess)
    play_again = input(
        f"You {game.status}! The word was {game.secret_word}. Play again? [Y/N]: "
    )
    if "Y" in play_again.upper():
        main()
    else:
        print("Thanks for playing!")
