"""Hangman. You know, like the game?"""

import json
import random
import string
from typing import ClassVar, Literal

from hangman import WORKING_DIRECTORY

ALPHABET = set(string.ascii_uppercase)
with (WORKING_DIRECTORY / "data" / "words.txt").open() as file:
    BANK: list[str] = file.read().splitlines()[1:]
with (WORKING_DIRECTORY / "data" / "hung_men.json").open() as file:
    HUNG_MEN: list[str] = json.load(file)

Status = Literal["in-progress", "won", "lost"]


class Hangman:
    """A game of hangman."""

    AUTOPRINT: ClassVar[bool] = False
    """Print man to be hung upon repr() call."""

    def __init__(self, bank: list[str] | None = None) -> None:
        """Create a game of hangman."""
        bank_ = BANK if bank is None else bank
        self.secret_word = random.choice(bank_)  # noqa: S311
        self.misses_remaining = 7
        self._status: Status = "in-progress"
        self.letters_found = [None] * len(self.secret_word)
        self._previous_guesses: set[str] = set()

    def __repr__(self) -> None:
        """Represent Hangman object as string."""
        return (
            f"Hangman(letters_found='{self.guessed}', "
            f"misses_remaining={self.misses_remaining}, "
            f"status='{self.status}')"
        )

    @property
    def guessed(self) -> str:
        """A string representation of the guessed letters."""
        result = ""
        for char in self.letters_found:
            result += "_" if char is None else char
        return result

    @property
    def letter_bank(self) -> str:
        """Letters not yet guessed."""
        return "".join(sorted(ALPHABET - self._previous_guesses))

    @property
    def status(self) -> Status:
        """Status of the game."""
        if self.misses_remaining == 0:
            self.status = "lost"
        return self._status

    @status.setter
    def status(self, value: Status) -> None:
        self._status = value

    def guess(self, char_or_word: str) -> None:
        """Submit a guess."""
        char_or_word = char_or_word.upper()
        if char_or_word in self._previous_guesses:
            return None
        if len(char_or_word) == 1:
            self._previous_guesses.add(char_or_word)
            if char_or_word in self.secret_word:
                for i, char in enumerate(self.secret_word):
                    if char == char_or_word:
                        self.letters_found[i] = char
            else:
                self.misses_remaining -= 1
        elif char_or_word == self.secret_word:
            self.letters_found = self.secret_word
            self.status = "won"
        else:
            self.misses_remaining -= 1

    def print(self, *, include_letters: bool = True) -> None:
        """Print the man to be hung."""
        print(HUNG_MEN[self.misses_remaining])
        if include_letters:
            print(self.guessed)
            print(f"Letter bank: {self.letter_bank}")
