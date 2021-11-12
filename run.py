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
computers_used_guess = []
bullets = 20
users_ships_remaining = 4
computers_ships_remaining = 4
ship_A = []
ship_B = []
ship_C = []
ship_D = []
ship_E = []
ship_F = []
ship_G = []
ship_H = []


def welcome():
    """
    function to clear the console, then to get the Username from the
    user and issue welcome message.
    """
    clear()
    print()
    print('-----------------------------------\n')
    print("Welcome to Brian's battleship game.\n")
    print('-----------------------------------')
    user = input('Enter your name here:\n')
    print(f"Welcome {user}, good luck, you'll need it")
    return user


def game_rules():
    """
    Function to display the game instructions prior to the game starting.
    """
    sleep(1)
    clear()
    print("-----------------------BRIANS BATTLESHIP GAME-----------------\n")
    print('Players get 4 ships each.')
    print('Each ship is 2 characters wide.')
    print('Each Player gets 20 torpedos.')
    print('Player goes first, then its the computers turn.\n')
    print('-------------------------GAME INSTRUCTIONS---------------------\n')
    print('Guess the co-ordinates of your opponents ship.')
    print('Top left corner is row: 1, column: 1.')
    print('Enter the co-ordinates and press Enter key to fire.')
    print('Each torpedo fired on target is marked with " @ ".')
    print('Each torpedo that is a miss is marked with " X ".')
    input('When you are ready, press the enter key to continue')
    print("Great, it's time to obliterate your enemy")
    sleep(1)


def init_game_boards(user):
    """
    Function to create the game board and to call the
    functions to place the users and computers ships at
    random locations throughout the boards.
    """
    clear()
    for rowcol in range(0, 10):
        game_board.append([' . '] * 10)
        computers_game_board.append([' . '] * 10)
    init_ships(game_board)
    init_ships(computers_game_board)
    return user


def print_game_board(user):
    """
    Function to print gameboard to console after the
    positions have been assigned for the users and computers ships.the function
    also prints the two game boards inline for the user to visually see
    both boards simultaniously throughout the game.
    """
    print("-----------------------BRIANS BATTLESHIP GAME-------------------\n")
    for rowcol in range(0, 10):
        print(''.join(game_board[rowcol]) + '\t\t' + ''.join(computers_game_board[rowcol]))
    print(f"{user}'s game board" + '\t\t\t\t' + "Computer's game board \n")
    users_guess(user)


def random_row(game_board):
    """
    Function to return random row position within the game board
    to position ships
    """
    return randint(0, len(game_board[0]) - 1)


def random_col(game_board):
    """
    Function to return random column position within the game board
    to position ships
    """
    return randint(0, len(game_board[0]) - 1)


def init_ships(a_game_board):
    """
    Function to randomly place computers and players ships
     on a given game board,assign ship location to variable
     and store ship location in global variable
    """
    if a_game_board == game_board:
        user_ship1 = place_ship('-DD', a_game_board, used_rows, used_cols)
        location_of_ship('A', user_ship1)
        user_ship2 = place_ship('-OO', a_game_board, used_rows, used_cols)
        location_of_ship('B', user_ship2)
        user_ship3 = place_ship('-88', a_game_board, used_rows, used_cols)
        location_of_ship('C', user_ship3)
        user_ship4 = place_ship('-00', a_game_board, used_rows, used_cols)
        location_of_ship('D', user_ship4)
    else:
        computer_ship1 = place_ship(' 1 ', a_game_board, used_rows, used_cols)
        location_of_ship('E', computer_ship1)
        computer_ship2 = place_ship(' 2 ', a_game_board, used_rows, used_cols)
        location_of_ship('F', computer_ship2)
        computer_ship3 = place_ship(' 3 ', a_game_board, used_rows, used_cols)
        location_of_ship('G', computer_ship3)
        computer_ship4 = place_ship(' 4 ', a_game_board, used_rows, used_cols)
        location_of_ship('H', computer_ship4)


def place_ship(char, a_game_board, used_rows, used_cols):
    ship_row = random_row(a_game_board)
    if ship_row not in used_rows:
        used_rows.append(ship_row)
    ship_col = random_col(a_game_board)
    if ship_col not in used_cols:
        used_cols.append(ship_col)
    ship_col2 = ship_col + 1
    if ship_col2 not in used_cols:
        ship_col2 = ship_col + 1
        if ship_col2 > 8:
            ship_col2 = ship_col - 1
            used_cols.append(ship_col2)
        else:
            used_cols.append(ship_col2)
    else:
        used_cols.append(ship_col2)

    if a_game_board == game_board:
        a_game_board[ship_row][ship_col] = char
        a_game_board[ship_row][ship_col2] = char
        ship = ship_row, ship_col
        ship_ = ship_row, ship_col2
        return ship, ship_

    if a_game_board == computers_game_board:
        a_game_board[ship_row][ship_col] = char
        a_game_board[ship_row][ship_col2] = char
        ship = ship_row, ship_col
        ship_ = ship_row, ship_col2
        return ship, ship_


def location_of_ship(ship, place):
    ships = list(place)
    global ship_A
    global ship_B
    global ship_C
    global ship_D
    global ship_E
    global ship_F
    global ship_G
    global ship_H

    if ship == 'A':
        ship_A = ships
    elif ship == 'B':
        ship_B = ships
    elif ship == 'C':
        ship_C = ships
    elif ship == 'D':
        ship_D = ships
    elif ship == 'E':
        ship_E = ships
    elif ship == 'F':
        ship_F = ships
    elif ship == 'G':
        ship_G = ships
    elif ship == 'H':
        ship_H = ships


def users_guess(user):
    global bullets
    while bullets > 0:
        print(ship_E, ship_F, ship_G, ship_H)
        print("Torpedo's remaining:", bullets)
        print(f"Players ships remaining:{users_ships_remaining}                 Computers ships remaining: {computers_ships_remaining}")
        guess_row = int(input("Guess Row: "))-1
        while guess_row > 10:
            print('Please enter a number from 1 to 10')
            guess_row = int(input("Guess Row: "))-1
        guess_col = int(input("Guess column: "))-1
        while guess_col > 10:
            print('Please enter a number from 1 to 10')
            guess_col = int(input("Guess column: "))-1
        guess = (guess_row, guess_col)
        if guess in users_used_guess:
            print('you fired here before! Please try again:')
            guess_row = int(input("Guess Row: "))-1
            guess_col = int(input("Guess column: "))-1
        users_used_guess.append(guess)
        print(f"{user} guessed row: {guess_row}, column: {guess_col}")
        hit_or_miss = shots_fired(guess)
        print_board_char(hit_or_miss, guess_row, guess_col)
        bullets -= 1
        sleep(2)
        clear()
        print_game_board(user)


def shots_fired(guess):
    global computers_ships_remaining
    hit = 'hit'
    miss = 'miss'
    if guess in ship_E:
        ship_E.remove(guess)
        if not ship_E:
            computers_ships_remaining -= 1
            print(f'Direct hit, ship sinking, computer only has {computers_ships_remaining} battleships remaining')
            return hit
        else:
            print('Direct hit, computers ship defenses are down')
            return hit
    elif guess in ship_F:
        ship_F.remove(guess)
        if not ship_F:
            computers_ships_remaining -= 1
            print(f'Direct hit, ship sinking, computer only has {computers_ships_remaining} battleships remaining')
            return hit
        else:
            print('Direct hit, computers ship defenses are down')
            return hit
    elif guess in ship_G:
        ship_G.remove(guess)
        if not ship_G:
            computers_ships_remaining -= 1
            print(f'Direct hit, ship sinking, computer only has {computers_ships_remaining} battleships remaining')
            return hit
        else:
            print('Direct hit, computers ship defenses are down')
            return hit
    elif guess in ship_H:
        ship_H.remove(guess)
        if not ship_H:
            computers_ships_remaining -= 1
            print(f'Direct hit, ship sinking, computer only has {computers_ships_remaining} battleships remaining')
            return hit
        else:
            print('Direct hit, computers ship defenses are down')
            return hit
    else:
        print('You Missed')
        return miss


def print_board_char(hit, guess_row, guess_col):
    if hit == 'hit':
        computers_game_board[guess_row][guess_col] = ' @ '
    elif hit == 'miss':
        computers_game_board[guess_row][guess_col] = ' X '


def clear():
    """
    Function to clear the terminal to keep playing
    area free from unused code,obtained from geeks for geeks.
    """
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def main():
    """
    Function to run all game functions
    """
    username = welcome()
    game_rules()
    user = init_game_boards(username)
    print_game_board(user)


main()
