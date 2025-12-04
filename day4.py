import copy


def has_paper_roll(
    row_i: int, col_i: int, matrix: list[list[int]], n_rows: int, n_cols: int
) -> int:
    if row_i >= 0 and col_i >= 0 and row_i < n_rows and col_i < n_cols:
        return 1 if matrix[row_i][col_i] == "@" else 0

    return 0


def solve_puzzle_brute_force(rows: list[str]) -> int:
    """
    Originally planned to use it to compare with the smart solution, but
    not being able to make the smart solution work lol.
    """
    n_rows = len(rows)
    n_cols = len(rows[0])
    result = 0

    for row in range(n_rows):
        for col in range(n_cols):
            if row == 0 and col == 7:
                print("here")
            acum = 0
            if rows[row][col] != "@":
                continue
            acum += has_paper_roll(row, col - 1, rows, n_rows, n_cols)
            acum += has_paper_roll(row, col + 1, rows, n_rows, n_cols)
            acum += has_paper_roll(row - 1, col, rows, n_rows, n_cols)
            acum += has_paper_roll(row - 1, col - 1, rows, n_rows, n_cols)
            acum += has_paper_roll(row - 1, col + 1, rows, n_rows, n_cols)
            acum += has_paper_roll(row + 1, col, rows, n_rows, n_cols)
            acum += has_paper_roll(row + 1, col - 1, rows, n_rows, n_cols)
            acum += has_paper_roll(row + 1, col + 1, rows, n_rows, n_cols)
            if acum < 4:
                result += 1

    return result


def solve_puzzle_brute_force_part2(rows: list[str]) -> int:
    """
    Pretty yucky solution, but it works and don't know why the smart
    solution doesn't work.
    """
    n_rows = len(rows)
    n_cols = len(rows[0])
    result = 0

    modified = True

    while modified:
        modified = False
        for row in range(n_rows):
            for col in range(n_cols):

                acum = 0
                if rows[row][col] != "@":
                    continue
                acum += has_paper_roll(row, col - 1, rows, n_rows, n_cols)
                acum += has_paper_roll(row, col + 1, rows, n_rows, n_cols)
                acum += has_paper_roll(row - 1, col, rows, n_rows, n_cols)
                acum += has_paper_roll(row - 1, col - 1, rows, n_rows, n_cols)
                acum += has_paper_roll(row - 1, col + 1, rows, n_rows, n_cols)
                acum += has_paper_roll(row + 1, col, rows, n_rows, n_cols)
                acum += has_paper_roll(row + 1, col - 1, rows, n_rows, n_cols)
                acum += has_paper_roll(row + 1, col + 1, rows, n_rows, n_cols)
                if acum < 4:
                    modified = True
                    result += 1
                    rows[row] = rows[row][:col] + "X" + rows[row][col + 1 :]

    return result


def update_neighbour_positions(
    row_i: int,
    col_i: int,
    value_matrix: list[list[int]],
    matrix: list[list[int]],
    n_rows: int,
    n_cols: int,
) -> list[list[int]]:
    if (
        row_i - 1 >= 0
        and col_i + 1 < n_cols
        and value_matrix[row_i - 1][col_i + 1] == "@"
    ):
        matrix[row_i - 1][col_i + 1] += 1

    if col_i + 1 < n_cols and value_matrix[row_i][col_i + 1] == "@":
        matrix[row_i][col_i + 1] += 1

    if row_i + 1 < n_rows:
        if value_matrix[row_i + 1][col_i] == "@":
            matrix[row_i + 1][col_i] += 1
        if col_i + 1 < n_cols and value_matrix[row_i + 1][col_i + 1] == "@":
            matrix[row_i + 1][col_i + 1] += 1

    return matrix


def solve_puzzle(rows: list[str]) -> int:
    """
    We can reduce the amount of rows we need to visit by looking always to the right and down.
    When we are looking there, we can update the positions of the neighbours.

    y y y y y y
    y y y y y y
    x x x x x x
    x x x x x x

    FOR SOME REASON DOESNT WORK: TODO: FIX
    """

    n_rows = len(rows)
    n_cols = len(rows[0])
    print("Rows:", n_rows, ", Cols: ", n_cols)
    sol_matrix = [[0] * n_cols for _ in range(n_rows)]

    acum = 0

    for i in range(n_rows):
        for j in range(n_cols):
            if i == 0 and j == 2:
                print("here")

            if rows[i][j] == "@":
                sol_matrix = update_neighbour_positions(
                    i, j, rows, sol_matrix, n_rows, n_cols
                )
                sol_matrix[i][j] = (
                    has_paper_roll(i, j, sol_matrix, n_rows, n_cols)
                    + has_paper_roll(i, j + 1, rows, n_rows, n_cols)
                    + has_paper_roll(i + 1, j, rows, n_rows, n_cols)
                    + has_paper_roll(i + 1, j + 1, rows, n_rows, n_cols)
                    + has_paper_roll(i - 1, j + 1, rows, n_rows, n_cols)
                )

    for i in range(n_rows):
        for j in range(n_cols):
            if sol_matrix[i][j] < 4:
                acum += 1

    print(sol_matrix)
    return acum


if __name__ == "__main__":
    fh = open("inputs/input_4.txt")
    # fh = open("inputs/test_input.txt")
    rows = []
    for line in fh:
        rows.append(line.strip())

    sol_brute = solve_puzzle_brute_force(rows)
    sol_smart = solve_puzzle(rows)

    sol_part2 = solve_puzzle_brute_force_part2(rows)

    print("====================================")
    print("Part 1 solution (Brute): ", sol_brute)
    print("Part 1 solution (Smart): ", sol_smart)
    print("Part 2 solution (Brute): ", sol_part2)
    print("====================================")
    fh.close()
