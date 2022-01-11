'''Generates a random number'''
from random import randint


def build_board(coords):
    '''Takes board coordinates
Returns board.
'''
    return [['O' for count in range(coords)] for count in range(coords)]


build_board(5)


def print_board(board):
    '''Prints board to terminal
Returns printed board to terminal'''

    for b_e in board:
        print(*b_e)


board1 = build_board(5)
print_board(board1)
print('Welcome to Battleship!!'
      'The object of the game is to sink the computers ships \n')
NAME = input('Enter your name: \n')
print(f'hello {NAME}')


def random_row(board):
    '''Prints Board
Returns board with functionality.
'''

    return randint(0, len(board) - 1)


def random_column(board):
    '''Creates the conditions for the game
Returns the method in how to play the game
'''
    return randint(0, len(board[0]) - 1)


def game():
    '''Shows the means how to play game with messaging'''
    ship_row = random_row(board1)
    ship_column = random_column(board1)
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
        elif (guess_row < 0 or guess_row > 4) or\
             (guess_column < 0 or guess_column > 4):
            print('Missed by miles ,that is not even close.')
        elif board1[guess_row][guess_column] == 'X':
            print('You guessed that already')
        else:
            print('You have missed')
            board1[guess_row][guess_column] = 'X'
            print_board(board1)

        print_board(board1)
        guesses = guesses + 1
    print('Game over')


while True:
    game()
    play_again = input(f'Would you like to play again {NAME} y/n: \n')
    # Returns a string wirth the name of the player
    if play_again.lower() == 'n':
        print('Goodbye!')
        break

