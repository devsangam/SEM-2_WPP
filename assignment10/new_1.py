import numpy as np
import random
def is_safe(board, row, col):
    if 1 in board[row]:
        return False
    
    if 1 in board[:, col]:
        return False
    
    sum_index = row + col
    for i in range(8):
        j = sum_index - i
        if 0 <= j < 8 and 0 <= i < 8:
            if board[i][j] == 1:
                return False
    
    diff_index = row - col
    for i in range(8):
        j = i - diff_index
        if 0 <= j < 8 and 0 <= i < 8:
            if board[i][j] == 1:
                return False
    
    return True

def solve_queens_backtracking(board, col=0):
    if col >= 8:
        return True
    
    rows = list(range(8))
    random.shuffle(rows)
    for row in rows:
        if is_safe(board, row, col):
            board[row][col] = 1
            
            if solve_queens_backtracking(board, col + 1):
                return True
            
            board[row][col] = 0  
    
    
    return False


board = np.zeros((8, 8), dtype=int)
solve_queens_backtracking(board)
for i in range(8):
    for j in range(8):       
        if(board[i][j]==0):
            print('.', end=" ")
        elif(board[i][j]==1):
            print('||', end=' ')
    print()
