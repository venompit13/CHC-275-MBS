""" 
Mitch Schauer
Section 02
Lab 6: Connect4.py
"""

""" 
Scenario: We are to build a connect 4 game that runs in the terminal
"""

def drawBoard(board):
    for row in board:
        for space in row:
            print(space, end="")
        print()

def switchPlayer(player):
    if player == "O":
        return "X"
    elif player == "X":
        return "O"
    
def dropPiece(board,player,col):
    for i in range(len(board)):
        if board[0][col] != 0:
            return False
    check = True
    while check == True:
        if board[i][col] == player:
            i = i + 1
        else:
            board[i-1] = player
            return True
    for i in range(len(board)):
        board[i][col] = player
        
        

def checkWinner(board,player):
    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2] == player:
            print (f"{player} wins")
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        print(f"{player} wins")
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        print(f"{player}wins")
        return True
    for row in board:
        for space in row:
            if space == 0:
                return False
    return True

def main():
    curr = "X"
    rows = 6
    cols = 7
    board = [
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
    ]
    player = "X"
    while checkWinner(board,curr) != True:
        curr = switchPlayer(curr)
        drawBoard(board)
        x = int(input("Enter Row: ").strip())
        y = int(input("Enter Col: ").strip())
        dropPiece(x,y,board,curr)
    
if __name__ == "__main__":
    main()