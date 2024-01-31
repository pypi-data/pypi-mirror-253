"""Hangman."""

from pathlib import Path

WORKING_DIRECTORY = (
    Path(__file__).parent if "__file__" in globals() else Path("hungmen")
)
