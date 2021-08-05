# Create board with coodinates

from random import randint

board = []

for i in range(0,10):
    board.append(["0"]*10)

print(board)

def print_board(board):
    for i in board:
        print(*i)

print("Let's play Battleship\n")
print_board(board)



# Create ships on the board 


def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)


ship_row = random_row(board)
ship_col = random_col(board)
guess_row = int(input("Guess Row:"))
guess_col = int(input("Guess Col:"))

print(ship_row)
print(ship_col)



#inp = input("Where do you want to shoot")
#x, y inp.split(", ")
#print(x)
#print(y)

#)

 


