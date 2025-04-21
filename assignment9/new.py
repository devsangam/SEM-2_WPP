import numpy as np

def is_safe(chess_board, row, col):
    # Check this row on the left side.
    for i in range(col):
        if chess_board[row][i] == 1:
            return False

    # Check upper diagonal on left side.
    i, j = row, col
    while i >= 0 and j >= 0:
        if chess_board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal on left side.
    i, j = row, col
    while i < 8 and j >= 0:
        if chess_board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def solve_queens(chess_board, col=0):
    # If all queens are placed then return True.
    if col >= 8:
        return True

    # Consider this column and try placing a queen in all rows one by one.
    for row in range(8):
        if is_safe(chess_board, row, col):
            # Place this queen in chess_board[row][col].
            chess_board[row][col] = 1

            # Recur to place the rest of the queens.
            if solve_queens(chess_board, col + 1):
                return True

            # If placing queen in chess_board[row][col] doesn't lead to a solution,
            # then remove the queen (backtrack).
            chess_board[row][col] = 0

    # If the queen cannot be placed in any row in this column, return False.
    return False

# Initialize the chess board.
chess_board = np.zeros((8, 8), dtype=int)

if solve_queens(chess_board):
    print("One solution for the eight queens problem:")
    print(chess_board)
else:
    print("Cannot place all Queens")
