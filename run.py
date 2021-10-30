"""
Create board with coordinates
"""

from random import randint

"""
Create board with coordinates
"""


def build_board(coords):
    return [['O' for count in range(coords)] for count in range(coords)]


build_board(5)


def print_board(board):
    for b in board:
        print(*b)


board = build_board(5)
print_board(board)
print('Welcome to Battleship!!' 'The object of the game is to sink the computers ships \n')
NAME = input("Enter your name: \n")
print(f"hello {NAME}")
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
    guess_row = int(input("Guess Row: \n"))
    guess_col = int(input("Guess Col: \n"))
    print(ship_row)
    print(ship_col)

    """
    Create conditions for game
    """
    if guess_row == ship_row and guess_col == ship_col:
        print("You've hit a battlship!")
        break
    elif (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
        print("Missed by miles ,that's not even close.")
    elif board[guess_row][guess_col] == "X":
        print("You guessed that already")
    else:
        print("You've missed")
        board[guess_row][guess_col] = "X"
        print_board(board)
        guesses = guesses + 1
    if guesses == 4:
        print("Game over")
    print_board(board)
        
