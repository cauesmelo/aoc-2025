"""Day 02:"""

from aoc.utils import read_split_by_comma


DAY = 2


def split_compare_str_by(s: str, split_by: int):
    str_size = len(s)

    parts = []

    count = 0
    step_size = str_size // split_by

    while count < str_size:
        parts.append(s[count : count + step_size])
        count += step_size

    compare_to = parts[0]

    for part in parts[1:]:
        if compare_to != part:
            return False, 0

    return True, int(s)


def part1(lines: list[str]) -> int:
    """Solve part 1."""

    res = 0

    for line in lines:
        id1, id2 = line.split("-")

        for i in range(int(id1), int(id2) + 1):
            str_i = str(i)

            if len(str_i) % 2 != 0:
                continue

            is_invalid, n = split_compare_str_by(str_i, 2)
            if is_invalid:
                res += n

    return res


def part2(lines: list[str]) -> int:
    """Solve part 2."""

    res = 0

    for line in lines:
        id1, id2 = line.split("-")

        for i in range(int(id1), int(id2) + 1):
            str_i = str(i)
            str_size = len(str_i)
            split_by = 2

            while split_by <= str_size:
                is_equal_parts = str_size % split_by == 0

                if is_equal_parts:
                    is_invalid, n = split_compare_str_by(str_i, split_by)

                    if is_invalid:
                        res += n
                        break

                split_by += 1

    return res


def main():
    lines = read_split_by_comma(DAY)

    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")


if __name__ == "__main__":
    main()
