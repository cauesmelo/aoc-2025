"""Day 07:"""

from aoc.utils import read_lines


DAY = 7


def part1(lines: list[str]) -> int:
    """Solve part 1."""

    chs: list[list[str]] = []

    for line in lines:
        list_of_ch = []
        for ch in line:
            list_of_ch.append(ch)

        chs.append(list_of_ch)

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


def part2(lines: list[str]) -> int:
    """Solve part 2."""
    return 0


def main():
    lines = read_lines(DAY, example=False)

    print(f"Part 1: {part1(lines)}")
    # print(f"Part 2: {part2(lines)}")


if __name__ == "__main__":
    main()
