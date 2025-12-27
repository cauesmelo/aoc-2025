"""Day 09:"""

from aoc.utils import read_lines


DAY = 9


def read_coordinate(line: str) -> tuple[int, int]:
    return tuple(int(coord) for coord in line.split(","))


def area_between_coordinates(c1: tuple[int, int], c2: tuple[int, int]) -> int:
    x = abs(c1[0] - c2[0]) + 1
    y = abs(c1[1] - c2[1]) + 1
    return x * y


def part1(lines: list[str]) -> int:
    """Solve part 1."""
    coordinates = [read_coordinate(line) for line in lines]

    largest_area = 0

    for c in coordinates:
        for c2 in coordinates:
            if c == c2:
                continue

            area = area_between_coordinates(c, c2)
            largest_area = max(largest_area, area)

    return largest_area


def part2(lines: list[str]) -> int:
    """Solve part 2."""
    return 0


def main():
    lines = read_lines(DAY, example=False)

    print(f"Part 1: {part1(lines)}")
    # print(f"Part 2: {part2(lines)}")


if __name__ == "__main__":
    main()
