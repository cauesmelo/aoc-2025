"""Day 01:"""

import math
from aoc.utils import read_lines


DAY = 1


def part1(lines: list[str]) -> int:
    """Solve part 1."""

    dial_pos = 50
    password = 0

    for line in lines:
        # print("The dial is", dial_pos, end="")
        # print("\t|| rotated", line, end="")
        value = int(line[1:])

        if line.startswith("L"):
            dial_pos = (dial_pos - value) % 100

        else:
            dial_pos = (dial_pos + value) % 100

        # print("\t|| to point at", dial_pos)

        if dial_pos == 0:
            password += 1

    return password


def part2(lines: list[str]) -> int:
    """Solve part 2."""

    dial_pos = 50
    password = 0

    for line in lines:
        print("The dial is", dial_pos, end="")
        print("\t|| rotated", line, end="")
        value = int(line[1:])

        clicked = False

        if line.startswith("L"):
            diff = dial_pos - value

            if diff < 0:
                clicks = math.ceil(-diff / 100)

                if clicks > 0:
                    clicked = True

                password += clicks
                print("\t|| clicks", clicks, end="")
            else:
                print("\t|| no clicks", end="")

            dial_pos = diff % 100

            print("\t|| diff", diff, end="")

        else:
            diff = dial_pos + value

            if diff > 100:
                clicks = abs(math.ceil(-diff / 100))

                if clicks > 0:
                    clicked = True

                password += clicks
                print("\t|| clicks", clicks, end="")
            else:
                print("\t|| no clicks", end="")

            dial_pos = diff % 100
            print("\t|| diff", diff, end="")

        print("\t|| to point at", dial_pos, end="")

        if dial_pos == 0 and clicked is False:
            print("\t|| add to password")
            password += 1
        else:
            print()

        clicked = False

    return password


def main():
    # lines = read_lines(DAY)
    lines = read_lines(DAY, filename="example.txt")

    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")


if __name__ == "__main__":
    main()
