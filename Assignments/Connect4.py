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
    if board[0][col] != 0:
        print("Not possible!")
        return False
    i = 0
    while i < len(board):
        if board[i][col] == 0:
            i = i + 1
        else:
            board[i-1][col] = player
            return True
    board[i-1][col] = player
    return True
        
        

def checkWinner(board,player):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == board[i][j+1] == board[i][j+2] == board[i](j+3) == player:
                print (f"{player} wins")
                return True
            if board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j] == player:
                print(f"{player} wins")
                return True
            if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] == player:
                print(f"{player}wins")
                return True
            if board[i][j] == board[i+1][j-1] == board[i+2][j-2] == board[i+3][j-3] ==player:
                print(f"{player} wins")
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
    while checkWinner(board,player) != True:
        player = switchPlayer(player)
        drawBoard(board)
        y = int(input("Enter Col: ").strip())
        dropPiece(board,player,y)
    
if __name__ == "__main__":
    main()