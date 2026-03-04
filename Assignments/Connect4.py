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
    ROWS = 6
    COLUMNS = 7
    BOARD = [
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
    ]
    CURRENT_PLAYER = "X"
    CURRENT_PLAYER = switchPlayer()
    
if __name__ == "__main__":
    main()