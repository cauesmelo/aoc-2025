"""Utility functions for Advent of Code solutions."""

from pathlib import Path


def read_input(day: int, filename: str = "input.txt") -> str:
    """Read the input file for a given day."""
    day_folder = Path(__file__).parent / f"day{day:02d}"
    return (day_folder / filename).read_text().strip()


def read_lines(day: int, filename: str = "input.txt") -> list[str]:
    """Read the input file as a list of lines."""
    return read_input(day, filename).splitlines()


def read_ints(day: int, filename: str = "input.txt") -> list[int]:
    """Read the input file as a list of integers."""
    return [int(line) for line in read_lines(day, filename)]


def read_grid(day: int, filename: str = "input.txt") -> list[list[str]]:
    """Read the input file as a 2D grid of characters."""
    return [list(line) for line in read_lines(day, filename)]

