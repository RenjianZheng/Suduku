sudoku = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

row_len = len(sudoku[0])
col_len = len(sudoku)


def solver(su):
    loc = locate_empty(su)
    if not loc:
        return True
    else:
        row, col = loc

    for i in range(1, 10):
        if is_valid(su, i, (row, col)):
            su[row][col] = i

            if solver(su):
                return True

            su[row][col] = 0

    return False


def is_valid(su, num, position):
    # check row
    for i in range(row_len):
        if su[position[0]][i] == num and position[1] != i:
            return False

    # check col
    for i in range(col_len):
        if su[i][position[1]] == num and position[0] != i:
            return False

    # check square
    square_col = position[1] // 3
    square_row = position[0] // 3

    for i in range(square_row * 3, square_row * 3 + 3):
        for j in range(square_col * 3, square_col * 3 + 3):
            if su[i][j] == num and (i, j) != position:
                return False

    return True


def locate_empty(su):
    for i in range(col_len):
        for j in range(row_len):
            if su[i][j] == 0:
                return (i, j)  # row first, col second
    return None


def print_sudoku(su):
    for i in range(col_len):
        if i % 3 == 0 and i != 0:
            print("-" * 23)

        for j in range(row_len):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j != 8:
                print(str(su[i][j]) + " ", end="")
            else:
                print(su[i][j])