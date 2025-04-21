import numpy as np
chess_board=np.zeros((8,8))
attacked_boxes=np.zeros((8,8))
#equation of diagonals (i,j) : y=x-i+j, y=i+j-x
def place_queen(chess_board,attacked_boxes, j, i):
    attacked_boxes[:,i:i+1]+=1
    attacked_boxes[j:j+1,:]+=1
    for x in range(8):
        y1=x-i+j
        y2=i+j-x
        if(y1>=0 and y1<8):
            attacked_boxes[x][y1]+=1
        if(y2>=0 and y2<8):
            attacked_boxes[x][y2]+=1
    chess_board[j][i]=1
    attacked_boxes[j][i]=9

def unplace_queen(chess_board,attacked_boxes, j, i):
    attacked_boxes[:,i:i+1]-=1
    attacked_boxes[j:j+1,:]-=1
    for x in range(8):
        y1=x-i+j
        y2=i+j-x
        if(y1>=0 and y1<8):
            attacked_boxes[x][y1]-=1
        if(y2>=0 and y2<8):
            attacked_boxes[x][y2]-=1
    chess_board[j][i]=0

def check_placement(attacked_boxes, j, i):#checks if after placing queen, there are any conflicts
    for x in range(8):
        y1=x-i+j
        y2=i+j-x
        if(y1>=0 and y1<8):
            if(attacked_boxes[x][y1]>0):
                return False
        if(y2>=0 and y2<8):
            if(attacked_boxes[x][y2]>0):
                return False
    return True
avialble_columns=range(8)
bt=np.zeros(8, dtype=int)
queens=np.zeros(8, dtype=int)


def find_and_place(chess_board,attacked_boxes, row, bt ,queens):
    if row < 0:
        print("No solution found.")
        return False
    if(row>7):
        print(chess_board)
        return True
    queen_placed=False
    backtrack=bt[row]
    for j in range(8):
            if(check_placement(attacked_boxes,j,row) and queen_placed==False):
                if(backtrack>0):
                    backtrack-=1
                    continue
                place_queen(chess_board, attacked_boxes,j,row)
                queens[row]=j
                queen_placed=True
                bt [row+1:]=0
                break

    if find_and_place(chess_board, attacked_boxes, row + 1, bt, queens):
        return True        
    # print(chess_board)
    # print(attacked_boxes)
    # print("row:  ",row)
    unplace_queen(chess_board, attacked_boxes, j, row)
    queen_placed = False


    if(queen_placed==False):
        bt[row]+=1
    #     if row - 1 < 0:
    #         print("No solution found.")
    #         return
    #     unplace_queen(chess_board, attacked_boxes,row-1, queens[row-1])
    #     find_and_place(chess_board,attacked_boxes, row-1, bt, queens)
    # else:
    #     bt[row+1:]=0
    #     find_and_place(chess_board,attacked_boxes, row+1, bt, queens)

find_and_place(chess_board, attacked_boxes, 0, bt, queens)
        
#i=0
# while(i<8):
#     j=0
#     queen_placed=False
#     while(queen_placed==False and j<8):
#         while (j<8 and attacked_boxes[j][i]>0):
#             j+=1
#         if(check_placement(attacked_boxes,j,i) and j<8):
#             place_queen(chess_board, attacked_boxes,j,i)
#             queen_placed=True
#             print(chess_board)
#         else:
#             j+=1
#     if(queen_placed):
#         i+=1
#         backtrack=0
#     else:
#         backtrack=+1
#         unplace_queen(chess_board, attacked_boxes,j,i)
    
        
