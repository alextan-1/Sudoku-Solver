def print_board(board):
    for i in range(len(board)):
        #Horizontal Borders
        if i % 3 == 0 and i != 0:
            print ('-----------------------')
        
        for j in range(len(board[0])):
            #Vertical Borders
            if j % 3 == 0 and j != 0:
                print (' | ', end="")
            #Print in next line if last index
            if j == 8:
                print (board[i][j])
            else:
                print (str(board[i][j]) + " ", end="")

def find(board):
    #Loop through board to unfilled boxes
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) #rol, col
    
    return None

def valid_ans(board, num, pos):
    #Checking if row is valid
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    
    #Checking if col is valid
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    
    #Checking if box of num is valid
    boxRow = pos[1] // 3
    boxCol = pos[0] // 3
    
    for i in range(boxCol*3, boxCol*3 + 3):
        for j in range(boxRow*3, boxRow*3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    
    return True

def solve(board):
    #If there are no empty boxes, puzzle is solved
    found = find(board)
    if not found:
        return True
    else:
        row, col = found
    
    #Solve puzzle with recursion
    for i in range(1,10):
        if valid_ans(board, i, (row, col)):
            board[row][col] = i
            
            if solve(board):
                return True
            
            board[row][col] = 0
    
    return False



board = [
         [7, 4, 9, 0, 0, 2, 8, 0, 0],
         [0, 0, 1, 9, 8, 0, 5, 0, 7],
         [8, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 3, 4, 0, 0, 1, 0, 0, 0],
         [5, 0, 6, 0, 2, 0, 7, 0, 3],
         [0, 0, 0, 6, 0, 0, 9, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 1],
         [6, 0, 8, 0, 3, 7, 4, 0, 0],
         [0, 0, 2, 4, 0, 0, 3, 7, 9]
        ]

print(" ")
print_board(board)
print(" ")
solve(board)
print_board(board)