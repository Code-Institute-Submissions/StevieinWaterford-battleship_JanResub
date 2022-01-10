
from random import randint

'''Takes board coordinates
Returns board.
'''


def build_board(coords):
    return [['O' for count in range(coords)] for count in range(coords)]


build_board(5)

'''Prints Board
Returns board with functionality.
'''


def print_board(board):
    for b in board:
        print(*b)


board = build_board(5)
print_board(board)
print('Welcome to Battleship!!'
      'The object of the game is to sink the computers ships \n')
NAME = input('Enter your name: \n')
print(f'hello {NAME}')

'''Creates ship on board
Retuns position of ship on the board.
'''


def random_row(board):
    return randint(0, len(board) - 1)


def random_column(board):
    return randint(0, len(board[0]) - 1)

'''Creates the conditions for the game
Returns the method in how to play the game
'''


def game():

    ship_row = random_row(board)
    ship_column = random_column(board)
    guesses = 0
    while guesses < 4:
        try:
            guess_row = int(input('Guess Row: \n'))
            guess_column = int(input('Guess Col: \n'))
        except ValueError:
            print('You have to enter a number, plesae try again.')
            continue
        print(ship_row)
        print(ship_column)
        if guess_row == ship_row and guess_column == ship_column:
            print('You have hit a battlship!')
            break
        elif (guess_row < 0 or guess_row > 4) or\
             (guess_column < 0 or guess_column > 4):
            print('Missed by miles ,that is not even close.')
        elif board[guess_row][guess_column] == 'X':
            print('You guessed that already')
        else:
            print('You have missed')
            board[guess_row][guess_column] = 'X'
            print_board(board)

        print_board(board)
        guesses = guesses + 1
    print('Game over')

while True:
    game()
    play_again = input(f'Would you like to play again {NAME} y/n: \n')
    if play_again.lower() == 'n':
        print('Goodbye!')
        break