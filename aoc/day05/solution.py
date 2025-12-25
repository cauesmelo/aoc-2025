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
        for r in fresh_range:
            if sku >= r[0] and sku <= r[1]:
                fresh_count += 1
                break

    return fresh_count


def part2(lines: list[str]) -> int:
    """Solve part 2."""
    fresh_range: list[tuple[int, int]] = []

    for line in lines:
        if line == "":
            break
        else:
            fresh_range.append(tuple(map(int, line.split("-"))))

    fresh_range.sort()

    merged = [fresh_range[0]]

    for start, end in fresh_range[1:]:
        last_start, last_end = merged[-1]

        if start <= last_end + 1:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))

    count = 0
    for start, end in merged:
        count += end - start + 1

    return count


def main():
    lines = read_lines(DAY, example=False)

    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")


if __name__ == "__main__":
    main()
