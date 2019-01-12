#Setting up the board
from IPython.display import clear_output #this works only in Jupyter

def display_board(board):
    from IPython.display import clear_output #this works only in Jupyter
    clear_output()
    #print('_________________________')
    print('|    '+'   |   '+' '+'   |   '+'    |')
    print('|   '+board[7]+'   |   '+board[8]+'   |   '+board[9]+'   |')
    print('|_______'+'|_______'+'|______'+'_|')
    print('|    '+'   |   '+' '+'   |   '+'    |')
    print('|   '+board[4]+'   |   '+board[5]+'   |   '+board[6]+'   |')
    print('|_______'+'|_______'+'|______'+'_|')
    print('|    '+'   |   '+' '+'   |   '+'    |')
    print('|   '+board[1]+'   |   '+board[2]+'   |   '+board[3]+'   |')
    print('|       '+'|       '+'|       '+'|')
    
#game_board = ['X']*10
#display_board(game_board)

#The player chooses his mark
def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
		
		
#Put the mark in the chosen position
def place_marker(board, marker, position):
    board[position] = marker
	
	
#Check if we have a winner
def win_check(board,mark):    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal


#Randomly decide who plays first
import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


#Checking if the chosen cell is free
def space_check(board, position):
    
    return board[position] == ' '


#Checking if the board is full 
def full_board_check(board):
    free_space = 0
    
    for i in range(1,10):
        if space_check(game_board, i):
            free_space += 1

    if free_space > 0:
        return False
    else:
        return True	
		
		
#Wanna play again?
def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

	
#The player chooses where to put on his mark
def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position
