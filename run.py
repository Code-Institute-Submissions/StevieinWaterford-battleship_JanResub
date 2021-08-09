"""
Create board with coordinates
"""

from random import randint

board = []

for i in range(0,5):
    board.append(["0"]*5)

print(board)

def print_board(board):
    for i in board:
        print(*i)


print("Let's play Battleship\n")
print_board(board)



"""
Create ship on the board
"""


def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)


ship_row = random_row(board)
ship_col = random_col(board)

guesses = 0
while guesses < 4:
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))

    print(ship_row)
    print(ship_col)

    """
    Create conditions for the game in terms of hits , misses and scope of the coordinates
    """


    if guess_row == ship_row and guess_col == ship_col:
        board[guess_row][guess_col] == "&"
        print("You've hit a battlship!")
        break

    elif (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
        print("Missed by a long shot ,that's not even in the ocean.")

    elif board[guess_row][guess_col] == "X":
        print("You guessed that already")


    else: 
        print("You've missed")
        board[guess_row][guess_col] = "X"
        print_board(board)
        guesses = guesses +1
        if guesses == 4:
            print("Game over")

        





#inp = input("Where do you want to shoot")
#x, y inp.split(", ")
#print(x)
#print(y)

#)

 


