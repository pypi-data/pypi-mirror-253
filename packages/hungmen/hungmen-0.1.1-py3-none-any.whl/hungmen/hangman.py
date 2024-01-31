"""Hangman. You know, like the game?"""
# TODO: Spaces are free.
import json
import random
import re
import string
from collections import UserList
from pathlib import Path
from typing import ClassVar, Literal

from hungmen import WORKING_DIRECTORY

ALPHABET = set(string.ascii_uppercase)
with (WORKING_DIRECTORY / "hung_men.json").open() as file:
    HUNG_MEN: list[str] = json.load(file)

Status = Literal["in-progress", "won", "lost"]


class WordBank(UserList[str]):
    """Import word bank from JSON list of strings."""

    def __init__(self, path: Path | str) -> None:
        """Create a WordBank from a JSON path."""
        self.path = Path(path)
        with self.path.open() as file:
            self.data = json.load(file)
        self.data = [word.upper() for word in self.data]

    def choose_random(self, pop: bool = True) -> str:
        """Pick a word at random. If `pop` is True, removes word from bank."""
        idx = random.randint(0, len(self) - 1)  # noqa: S311
        result = self.pop(idx) if pop else self[idx]
        return result


class Hangman:
    """A game of hangman."""

    AUTOPRINT: ClassVar[bool] = False
    """Print man to be hung upon repr() call."""

    def __init__(self, bank: WordBank) -> None:
        """Create a game of hangman."""
        self.secret_word = bank.choose_random()
        self.misses_remaining = 7
        self._status: Status = "in-progress"
        self.letters_found: list[str | None] = [
            (char if char not in string.ascii_uppercase else None)
            for char in self.secret_word
        ]
        self._previous_guesses: set[str] = set()

    def __repr__(self) -> str:
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
        if list(self.secret_word) == self.letters_found:
            self.status = "won"
        elif self.misses_remaining == 0:
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
            self.letters_found = list(self.secret_word)
            self.status = "won"
        else:
            self.misses_remaining -= 1

    def print(self, *, include_letters: bool = True) -> None:
        """Print the man to be hung."""
        print(HUNG_MEN[self.misses_remaining])
        if include_letters:
            print(self.guessed)
            print(f"Letter bank: {self.letter_bank}")
