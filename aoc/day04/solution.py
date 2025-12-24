"""Day 04:"""

from aoc.utils import read_lines


DAY = 4

DEBUG = False


def create_submatrix_3_by_3(
    matrix: list[list[str]], col_idx: int, row_idx: int
) -> list[list[str]]:
    submatrix = [["."] * 3 for _ in range(3)]

    for row_count in range(-1, 2):
        calc_row = row_idx + row_count
        if calc_row < 0 or calc_row >= len(matrix):
            continue

        for col_count in range(-1, 2):
            calc_col = col_idx + col_count
            if calc_col < 0 or calc_col >= len(matrix[0]):
                continue

            submatrix[row_count + 1][col_count + 1] = matrix[calc_row][calc_col]

    submatrix[1][1] = "x"
    return submatrix


def count_rolls(matrix: list[list[str]]):
    if DEBUG:
        print("Counting rolls in submatrix:")
        for row in matrix:
            for ch in row:
                print(ch, end=" ")
            print()
        print("---")
    count = 0
    for row in matrix:
        for ch in row:
            if ch == "@":
                count += 1

    if DEBUG:
        print(f"Counted {count} rolls")
        print("---")

    return count


def part1(lines: list[str]) -> int:
    matrix = [list(line) for line in lines]
    matrix_copy = [row.copy() for row in matrix]

    accessible_rolls = 0

    for row_idx, row in enumerate(matrix):
        for col_idx, ch in enumerate(row):
            if ch == "@":
                submx = create_submatrix_3_by_3(
                    matrix, col_idx=col_idx, row_idx=row_idx
                )
                count = count_rolls(submx)

                if count < 4:
                    accessible_rolls += 1
                    matrix_copy[row_idx][col_idx] = "x"

    if DEBUG:
        print("Final matrix:")
        for row in matrix_copy:
            for ch in row:
                print(ch, end=" ")
            print()
        print("---")

    return accessible_rolls


def part2(lines: list[str]) -> int:
    """Solve part 2."""
    return 0


def main():
    lines = read_lines(DAY, example=False)

    import os

    os.system("clear")

    print(f"Part 1: {part1(lines)}")
    # print(f"Part 2: {part2(lines)}")


if __name__ == "__main__":
    main()
