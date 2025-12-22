"""Day 03:"""

from aoc.utils import read_lines


DAY = 3


def get_bigger_number_in_list(line: list[str], skip: int):
    bigger = -1
    bigger_idx = 0

    for idx, ch in enumerate(line):
        if idx == len(line) - skip:
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
        na, na_idx = get_bigger_number_in_list(line, 1)
        nb, nb_idx = get_bigger_number_in_list(line[na_idx + 1 :], 0)

        sum += int(str(na) + str(nb))

    return sum


def part2(lines: list[str]) -> int:
    """Solve part 2."""
    sum = 0

    for line in lines:
        seq = ""
        start_idx = 0
        end_idx = len(line) - 11

        for _ in range(11, -1, -1):
            sliced_line = line[start_idx:end_idx]
            n, idx = get_bigger_number_in_list(sliced_line, skip=0)
            end_idx += 1
            start_idx += idx + 1
            seq += str(n)

        sum += int(seq)

    return sum


def main():
    lines = read_lines(DAY, example=False)

    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")


if __name__ == "__main__":
    main()
