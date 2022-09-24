def get_board():
    print("Puzzle?")
    board=input()
    return board


def StringToMatrix(board):
    pieces = [board[i] for i in range(0, len(board), 1)]
    for i in range(0, len(pieces)):
        pieces[i] = int(pieces[i])
    grid = [pieces[x:x+6] for x in range(0, len(pieces), 6)]
    return grid

def MatrixToString(grid):
    board = "".join("".join(map(str, cell)) for cell in grid)
    return board

#print(grid)
def possible(row, column, number,grid):
    #global grid
    #checks If the number appearing in the given row
    for i in range(0,6):
        if grid[row][i] == number:
            return False

    #Checks if  the number appearing in the given column
    for i in range(0,6):
        if grid[i][column] == number:
            return False
    
    # Checks If the number appearing in the given square?
    x0 = (column // 3) * 3
    y0 = (row // 2) * 2
    #print(x0,y0)
    for i in range(0,2):
        for j in range(0,3):
            if grid[y0+i][x0+j] == number:
                return False

    return True

def solve(grid):
    board = MatrixToString(grid)
    # print(board)
    if board.count('0') ==0:
        print(board)
        return True,board

    for row in range(0,6):
        for column in range(0,6):
            if grid[row][column] == 0:
                for number in range(1,7):
                    if possible(row, column, number,grid):

                        grid[row][column] = number

                        if solve(grid)[0]:

                            return True,board

                        grid[row][column] = 0
       
                return None,None


    result= MatrixToString(grid)
    conv_str=str(result)
    replace_comma=conv_str.replace(", ","")
    replace_bracket=replace_comma.replace("[","")
    final_replace=replace_bracket.replace("]","")
    return final_replace
 

if __name__ == "__main__":
    pointer = 0
    while True:
        board = get_board() 
        pointer += 1
        grid=StringToMatrix(board) 
        solve(grid)














    
            

