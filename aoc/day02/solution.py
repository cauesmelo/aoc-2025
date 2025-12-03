"""Day 02:"""

from aoc.utils import read_split_by_comma


DAY = 2


def is_invalid_id(id: str) -> bool:
    if len(id) % 2 != 0:
        return False

    half = len(id) // 2
    ptr1 = 0
    ptr2 = half

    while ptr1 < half:
        if id[ptr1] != id[ptr2]:
            return False

        ptr1 += 1
        ptr2 += 1

    return True


def part1(lines: list[str]) -> int:
    """Solve part 1."""

    invalid_ids = 0

    for line in lines:
        id1, id2 = line.split("-")

        for i in range(int(id1), int(id2) + 1):
            if is_invalid_id(str(i)):
                print("invalid -> ", i)
                invalid_ids += i

    return invalid_ids


def part2(lines: list[str]) -> int:
    """Solve part 2."""
    return 0


def main():
    # lines = read_split_by_comma(DAY, example=True)
    lines = read_split_by_comma(DAY)

    print(lines)

    print(f"Part 1: {part1(lines)}")
    # print(f"Part 2: {part2(lines)}")


if __name__ == "__main__":
    main()
