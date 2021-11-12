from random import randint
# import only system from os
from os import system, name
# import sleep to show output for some time period
from time import sleep


game_board = []
computers_game_board = []
used_rows = []
used_cols = []
users_used_guess = []
bullets = 20
users_ship_locations = {}
ship = []
ship_a1 = []
ship_a2 = []
ship_b1 = []
ship_b2 = []
ship_c1 = []
ship_c2 = []
ship_d1 = []
ship_d2 = []

ship_A1 = [] 
ship_A2 = []
ship_B1 = [] 
ship_B2 = []
ship_C1 = [] 
ship_C2 = []
ship_D1 = [] 
ship_D2 = []

def welcome():
    """
    function to get Username from the user and issue welcome message
    """
    clear()
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
    sleep(1)


def init_game_boards(user):
    for rowcol in range(0, 10):
        game_board.append([' . '] * 10)
        computers_game_board.append([' . '] * 10)
    init_ships(game_board)
    init_ships(computers_game_board)       
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
        user_ship1 = place_ship('-XX', a_game_board, used_rows, used_cols, ship_a1, ship_a2) 
        global ship_A1 = user_ship1      
        place_ship('-OO', a_game_board, used_rows, used_cols, ship_b1, ship_b2)
        place_ship('-88', a_game_board, used_rows, used_cols, ship_c1, ship_c2)
        place_ship('-00', a_game_board, used_rows, used_cols, ship_d1, ship_d2)
    else:
        place_ship(' 1 ', a_game_board, used_rows, used_cols, ship_A1, ship_A2)
        place_ship(' 2 ', a_game_board, used_rows, used_cols, ship_B1, ship_B2)
        place_ship(' 3 ', a_game_board, used_rows, used_cols, ship_C1, ship_C2)
        place_ship(' 4 ', a_game_board, used_rows, used_cols, ship_D1, ship_D2)


def place_ship(char, a_game_board, used_rows, used_cols, ship, ship_):
    ship_row = random_row(a_game_board)  
    if ship_row not in used_rows:
        used_rows.append(ship_row)
    ship_col = random_col(a_game_board)
    if ship_col not in used_cols:
        used_cols.append(ship_col) 
    ship_col2 = ship_col + 1
    if ship_col2 not in used_cols:
        if ship_col2 > 8:
            ship_col2 = ship_col - 1
            used_cols.append(ship_col2)
        else:
            used_cols.append(ship_col2)
    if a_game_board == game_board:         
        a_game_board[ship_row][ship_col] = char  
        a_game_board[ship_row][ship_col2] = char
        ship = (ship_row , ship_col)
        ship_ = (ship_row , ship_col2)
        return (ship, ship_)
        
        
        
    if a_game_board == computers_game_board:         
        a_game_board[ship_row][ship_col] = char
        a_game_board[ship_row][ship_col2] = char
    




def location_of_ship(ship):
    users_ship_locations.append(ship)

    




  

def users_guess(user):   
    global bullets  
    while bullets > 0:
        print("bullet's remaining:", bullets)
        guess_row = int(input("Guess Row: ") ) - 1 
        while guess_row > 10: 
            print('Please enter a number from 1 to 10')
            guess_row = int(input("Guess Row: ") ) - 1 
        guess_col = int(input("Guess column: ") ) - 1 
        while guess_col > 10: 
            print('Please enter a number from 1 to 10')
            guess_col = int(input("Guess column: ") ) - 1 
        guess = [guess_row, guess_col]
        users_used_guess.append(guess)             
        print(f"{user} guessed row: {guess_row + 1}, column: {guess_col + 1}")
        bullets -= 1     
        print_game_board(user)
        #     print('hit')
        # else:
        #     print('miss')
      
        





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
    sleep(1)
    clear()
    game_rules()
    clear()
    user = init_game_boards(username)
    print_game_board(user) 
   
    # print_game_board(user)     
         
    # print_game_board(user)  



main()

