"""
    Author:         CaptCorpMURICA
    Project:        RandomProjects
    File:           sudokuSolverBasic.py.py
    Creation Date:  12/20/19, 2:09 PM
    Description:    Basic, text driven Sudoku solver application that leverages backtracking for increased efficiency.
"""

# Enter the Sudoku board in the matrix below. Use `0` for unknown spaces.
# Blank board included in the comments below.
# board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0]
#          ]

board = [[0, 3, 0, 4, 0, 0, 8, 5, 0],
         [9, 0, 0, 0, 0, 0, 0, 0, 2],
         [0, 0, 0, 8, 0, 2, 0, 0, 0],
         [0, 0, 0, 0, 0, 7, 2, 1, 0],
         [6, 1, 7, 0, 0, 0, 0, 0, 0],
         [0, 0, 8, 0, 0, 0, 0, 0, 5],
         [0, 4, 0, 0, 0, 5, 9, 7, 0],
         [0, 7, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 9, 0, 6, 0]
         ]


def solve(brd):
    """
    Uses the matrix as an input, finds the location of the next empty field, uses the location to find a possible value
    and then validates it with the `valid()` function. If successful, the program moves to the next value. Otherwise, it
    returns previous entries to `0` and attempts to solve again. This process repeats until all values have been found.
    If there is no solution to the problem, the program returns False.

    :param brd: Matrix input of the board needed to solve for the Sudoku problem.
    :return: Returns True if a solution was successful and False if not.
    """
    find = find_empty(brd)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(brd, i, (row, col)):
            brd[row][col] = i

            if solve(brd):
                return True

            brd[row][col] = 0

    return False


def valid(brd, num, pos):
    """
    Compares the suggested value against the row, column, and 3x3 grid to identify if entry is valid. If the number is
    observed in either of these categories, the entry is invalid and the test fails. At that point, a new value is
    determined and the process repeats. If the entry is valid, the process advances to the next empty position.

    :param brd: Matrix input of the board needed to solve for the Sudoku problem.
    :param num: The entry into the position that is under review for validation.
    :param pos: Tuple row/column position of the position under review by the program.
    :return: True if valid entry, False if invalid entry.
    """
    # Check for row validation
    for i in range(len(brd[0])):
        if brd[pos[0]][i] == num and pos[1] != i:
            return False

    # Check for column validation
    for j in range(len(brd)):
        if brd[j][pos[1]] == num and pos[0] != j:
            return False

    # Check for 3x3 grid validation
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if brd[i][j] == num and (i, j) != pos:
                return False

    return True


def print_board(brd):
    """
    Formats the Sudoku board to improve readability over the matrix format.

    :param brd: Matrix input of the board needed to solve for the Sudoku problem.
    :return: Prints the formatted board to the terminal.
    """
    for i in range(len(brd)):
        if i % 3 == 0 and i != 0:
            print("-----------------------")

        for j in range(len(brd[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(brd[i][j])
            else:
                print(f"{brd[i][j]} ", end="")


def find_empty(brd):
    """
    Uses the Sudoku problem as a Matrix input and returns the row/column location of the next empty field.

    :param brd: Matrix input of the board needed to solve for the Sudoku problem.
    :return: The row/column of the next empty field as a tuple.
    """
    for i in range(len(brd)):
        for j in range(len(brd[0])):
            if brd[i][j] == 0:
                return i, j  # i: row, j: column
    return None


if __name__ == '__main__':
    print("Unsolved Sudoku:")
    print_board(board)
    solve(board)
    print("=======================")
    print("Solved Sudoku:")
    print_board(board)
