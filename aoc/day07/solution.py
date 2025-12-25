"""Day 07:"""

from aoc.utils import read_lines
from functools import lru_cache


DAY = 7


def part1(lines: list[str]) -> int:
    """Solve part 1."""

    chs = build_matrix(lines)

    height = len(chs)
    width = len(chs[0])

    split_count = 0

    for line in range(height):
        for col in range(width):
            ch = chs[line][col]

            if ch == "S":
                chs[line + 1][col] = "|"

            if ch == "|":
                has_space_below = line + 1 < height
                splitter_below = False

                if has_space_below and chs[line + 1][col] == "^":
                    splitter_below = True
                    split_count += 1

                has_space_right = col + 1 < width
                has_space_left = col - 1 >= 0

                if splitter_below:
                    if has_space_right:
                        chs[line + 1][col + 1] = "|"

                    if has_space_left:
                        chs[line + 1][col - 1] = "|"
                else:
                    if has_space_below:
                        chs[line + 1][col] = "|"

    return split_count


def build_matrix(lines: list[str]) -> list[list[str]]:
    chs: list[list[str]] = []
    for line in lines:
        list_of_ch = []
        for ch in line:
            list_of_ch.append(ch)
        chs.append(list_of_ch)
    return chs


def copy_matrix(chs: list[list[str]]) -> list[list[str]]:
    return [row.copy() for row in chs]


def run_timeline(chs: list[list[str]], start_line: int, start_col: int) -> int:
    height = len(chs)
    width = len(chs[0])

    @lru_cache(None)
    def dfs(line: int, col: int) -> int:
        while True:
            if line + 1 >= height:
                return 1

            next_ch = chs[line + 1][col]

            if next_ch == ".":
                line += 1
                continue

            if next_ch == "^":
                timelines = 0

                if col - 1 >= 0:
                    timelines += dfs(line + 1, col - 1)

                if col + 1 < width:
                    timelines += dfs(line + 1, col + 1)

                return timelines

            line += 1

    return dfs(start_line, start_col)


def part2(lines: list[str]) -> int:
    chs = build_matrix(lines)

    for r in range(len(chs)):
        for c in range(len(chs[0])):
            if chs[r][c] == "S":
                return run_timeline(chs, r, c)


def main():
    lines = read_lines(DAY, example=False)

    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")


if __name__ == "__main__":
    main()
