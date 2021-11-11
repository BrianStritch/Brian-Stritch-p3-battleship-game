from random import randint
# import only system from os
from os import system, name
# import sleep to show output for some time period
from time import sleep


game_board = []
computers_game_board = []
used_rows = []
used_cols = []
ship = []
shipA = []
shipA1 = []
shipA2 = []
shipB = []
shipC = []
shipD = []

def welcome():
    """
    function to get Username from the user and issue welcome message
    """
    print()
    print('------------------------------')
    print("Welcome to Brian's battleship game.")
    print('------------------------------')
    user = input('Enter your name here:\n')
    print(f"Welcome {user}, good luck, you'll need it")    
    return user


def game_rules():
    print("                      BRIANS BATTLESHIP GAME\n")    
    print('player and computer get 4 boats each.')
    print('Each boat is 2 charachters wide.')
    print('Each Player gets 20 torpidoes.')
    print('Player goes first, then its the computers turn.')
    print('                         GAME INSTRUCTIONS')
    print('Guess the co-ordinates of your oponents ship')
    print('Enter the co-ordinates and press Enter key to fire')
    accept = input('When you are ready to start, press the Enter key to continue')
    print("Great, it's time to obliterate your enemy")
    sleep(2)


def init_game_boards(user):
    for rowcol in range(0, 10):
        game_board.append([' . '] * 10)
        computers_game_board.append([' . '] * 10)

    init_ships(game_board)
    init_ships(computers_game_board)
    print_game_board(user)
    return user


def print_game_board(user):
    print("                       BRIANS BATTLESHIP GAME\n")
    for rowcol in range(0, 10):
        print(''.join(game_board[rowcol]) + '\t\t' + ''.join(computers_game_board[rowcol]))
    print(f"{user}'s game board" + '\t\t\t\t' + "Computer's game board \n")    
    users_guess(user)


def random_row(game_board):
    """
    Function to return random row position within the game board
    to position ships
    """
    return randint(0, len(game_board) - 1)


def random_col(game_board):
    """
    Function to return random column position within the game board
    to position ships
    """
    return randint(0, len(game_board[0]) - 1)


def init_ships(a_game_board):
    """
    Function to randomly place players ships on a given game board
    """
    if a_game_board == game_board:
        place_ship('-XX', a_game_board, used_rows, used_cols, ship)
        place_ship('-OO', a_game_board, used_rows, used_cols, ship)
        place_ship('-88', a_game_board, used_rows, used_cols, ship)
        place_ship('-00', a_game_board, used_rows, used_cols, ship)
    else:
        place_ship(' 1 ', a_game_board, used_rows, used_cols, shipA)
        place_ship(' 2 ', a_game_board, used_rows, used_cols, shipB)
        place_ship(' 3 ', a_game_board, used_rows, used_cols, shipC)
        place_ship(' 4 ', a_game_board, used_rows, used_cols, shipD)


def place_ship(char, a_game_board, used_rows, used_cols, ship):
    ship_row = random_row(a_game_board)  
    if ship_row not in used_rows:
        used_rows.append(ship_row)
    ship1_col = random_col(a_game_board)
    if ship1_col not in used_cols:
        used_cols.append(ship1_col) 
    ship1_col2 = ship1_col + 1
    if ship1_col2 not in used_cols:
        if ship1_col2 > 8:
            ship1_col2 = ship1_col - 1
            used_cols.append(ship1_col2)
        else:
            used_cols.append(ship1_col2)
    if a_game_board == game_board:         
        a_game_board[ship_row][ship1_col] = char
        a_game_board[ship_row][ship1_col2] = char
    if a_game_board == computers_game_board:         
        a_game_board[ship_row][ship1_col] = char
        a_game_board[ship_row][ship1_col2] = char
    
    
    






def users_guess(user):
    print(shipA1)
    print(shipA2)
    bullets = 20    
    while bullets > 0:
        print('bullets:', bullets)
        guess_row = int(input("Guess Row: "))
        guess_col = int(input("Guess Col: "))
        guess = [guess_row, guess_col]
        
        #     print('hit')
        # else:
        #     print('miss')
        bullets -= 1
        





#from geeks for geeks to clear console on execution of this function 

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')  

  




def main():
    """
    Function to run all game functions
    """
    username = welcome()
    sleep(2)
    clear()
    game_rules()
    clear()
    user = init_game_boards(username)
    
   
    # print_game_board(user)     
         
    # print_game_board(user)  



main()

