"""Utility functions for Advent of Code solutions."""

from pathlib import Path


def read_input(day: int, example=False, keep_ws=False) -> str:
    """Read the input file for a given day."""
    filename = "example.txt" if example else "input.txt"
    day_folder = Path(__file__).parent / f"day{day:02d}"
    if keep_ws:
        return (day_folder / filename).read_text()

    return (day_folder / filename).read_text().strip()


def read_lines(day: int, example=False, keep_ws=False) -> list[str]:
    """Read the input file as a list of lines."""
    return read_input(day, example, keep_ws).splitlines()


def read_ints(day: int, example=False) -> list[int]:
    """Read the input file as a list of integers."""
    return [int(line) for line in read_lines(day, example)]


def read_grid(day: int, example=False) -> list[list[str]]:
    """Read the input file as a 2D grid of characters."""
    return [list(line) for line in read_lines(day, example)]


def read_split_by_comma(day: int, example=False) -> list[str]:
    """Read the input file as a list of strings (lines representing the grid)."""
    return read_input(day, example).split(",")
