"""Day 03:"""

from aoc.utils import read_lines


DAY = 3


def get_bigger_number_in_list(line: list[str], first_pick: bool):
    bigger = -1
    bigger_idx = 0

    for idx, ch in enumerate(line):
        if first_pick and idx == len(line) - 1:
            continue

        n = int(ch)
        if n > bigger:
            bigger = n
            bigger_idx = idx

    return bigger, bigger_idx


def part1(lines: list[str]) -> int:
    """Solve part 1."""
    sum = 0

    for line in lines:
        na, na_idx = get_bigger_number_in_list(line, True)
        nb, nb_idx = get_bigger_number_in_list(line[na_idx + 1 :], False)

        sum += int(str(na) + str(nb))

    return sum


def part2(lines: list[str]) -> int:
    """Solve part 2."""
    return 0


def main():
    lines = read_lines(DAY, example=False)

    print(f"Part 1: {part1(lines)}")
    # print(f"Part 2: {part2(lines)}")


if __name__ == "__main__":
    main()
