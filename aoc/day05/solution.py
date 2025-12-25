"""Day 05:"""

from aoc.utils import read_lines


DAY = 5


def part1(lines: list[str]) -> int:
    """Solve part 1."""

    fresh_range: list[tuple[int, int]] = []
    skus: list[int] = []
    scanning_ranges = True

    for line in lines:
        if scanning_ranges:
            if line == "":
                scanning_ranges = False
            else:
                fresh_range.append(tuple(map(int, line.split("-"))))
        else:
            skus.append(int(line))

    fresh_count = 0

    for sku in skus:
        for range in fresh_range:
            if sku >= range[0] and sku <= range[1]:
                fresh_count += 1
                break

    return fresh_count


def part2(lines: list[str]) -> int:
    """Solve part 2."""
    return 0


def main():
    lines = read_lines(DAY, example=False)

    print(f"Part 1: {part1(lines)}")
    # print(f"Part 2: {part2(lines)}")


if __name__ == "__main__":
    main()
