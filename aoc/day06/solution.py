"""Day 06:"""

from aoc.utils import read_lines


DAY = 6


def part1(lines: list[str]) -> int:
    """Solve part 1."""
    problems = []

    for line in lines:
        values = [v for v in line.split(" ") if v]

        if len(problems) == 0:
            for val in values:
                problems.append([val])

        else:
            for idx, val in enumerate(values):
                problems[idx].append(val)

    total_sum = 0

    for p in problems:
        sum = int(p[0])
        if p[-1] == "*":
            for val in p[1:-1]:
                sum *= int(val)
        if p[-1] == "+":
            for val in p[1:-1]:
                sum += int(val)

        total_sum += sum

    return total_sum


def part2(lines: list[str]) -> int:
    """Solve part 2."""
    return 0


def main():
    lines = read_lines(DAY, example=False)

    print(f"Part 1: {part1(lines)}")
    # print(f"Part 2: {part2(lines)}")


if __name__ == "__main__":
    main()
