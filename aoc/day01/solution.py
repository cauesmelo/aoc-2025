"""Day 01:"""

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
        # print("The dial is", dial_pos, end="")
        # print("\t|| rotated", line, end="")
        value = int(line[1:])
        direction = line[0]

        current_clicks = 0

        for _ in range(value):
            if direction == "L":
                dial_pos = (dial_pos - 1) % 100
            else:
                dial_pos = (dial_pos + 1) % 100

            if dial_pos == 0:
                current_clicks += 1
                password += 1

        # print("\t|| clicks", current_clicks, end="")
        # print("\t|| to point at", dial_pos)

    return password


def main():
    lines = read_lines(DAY)
    # lines = read_lines(DAY, filename="example.txt")

    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")


if __name__ == "__main__":
    main()
