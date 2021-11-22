import gspread
from google.oauth2.service_account import Credentials

from random import randint

from os import system, name

from time import sleep


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('battleship_high_scores')
players_scores = SHEET.worksheet('players_scores')
highscore = SHEET.worksheet('highscore')


"""
Global variables required for use in multiple game functions
"""


user = ''
level = ''
users_score = 0
computers_score = 0
game_board = []
computers_game_board = []
used_rows = []
used_cols = []
users_used_guess = []
computers_used_guess = []
bullets = 20
computers_bullets = 20
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
ships_list = []


def welcome():
    """
    function to clear the console, then to get the Username from the
    user and issue welcome message.
    """
    global user
    global level
    global users_ships_remaining
    global computers_ships_remaining
    game_level = ''
    clear()
    print()
    print(
        '----------------------------------- Welcome to ' +
        '---------------------------------\n'
        )
    print(
        '---------------------------- BRIANS BATTLESHIP GAME ' +
        '----------------------------\n'
        )
    print(
        '-------------------------------------- 2021 ' +
        '------------------------------------\n'
        )
    while True:
        user_name = input(
            '                             ' +
            ' Enter your name here:\n'
            )
        if not user_name:
            print(
                '                           ',
                'Please enter a username.'
                )
        elif len(user_name) > 6:
            print(
                '            Please enter a username with ',
                'a maximum of 6 charachters please:'
                )
        elif user_name.isalpha():
            break        
        elif user_name.isalnum():
            print(
                '                       Please enter a ',
                'name without numbers:'
                )        
        elif user_name == 'exit':
            end_game()
            break
        else:
            break
    user = user_name.capitalize()
    print(f'                                    Welcome {user}')
    print('                                    Game Levels:')
    print(
        '                      Beginner = 1 ,' +
        ' Intermediate = 2 , Advanced = 3'
        )
    while True:
        level = input(
            '                           ' +
            'Please enter your chosen game level: \n'
            )
        levels = level
        num = check_num_input(levels)
        if num == 'True':
            if int(levels) > 0:
                if int(levels) < 4:
                    break
            print('Please enter a number between 1 and 3.')
    if level == '1':
        game_level = 'Beginner'
    elif level == '2':
        game_level = 'Intermediate'
    elif level == '3':
        game_level = 'Advanced'
    print(
        f"                         Welcome {user}, " +
        f"You chose level {level}, {game_level}"
        )
    print(
        '                             ' +
        'good luck, you will need it'
        )
    if level == '1':
        users_ships_remaining = 3
        computers_ships_remaining = 3
    sleep(2)
    return user


def game_rules():
    """
    Function to display the game description and
     instructions prior to the game starting.
    """
    sleep(1)
    clear()
    print()
    print(
        "--------------------------- BRIANS BATTLESHIP GAME --" +
        "---------------------------\n"
        )
    print('     level 1 Players get 3 ships each.')
    print('     level 2 and level 3 Players get 4 ships each.')
    print('     Each ship is 2 characters wide.')
    print('     Each Player gets 20 torpedos.')
    print('     Player goes first, then its the computers turn.')
    print('     Each player gets 300 points per target hit.')
    print('     Additional 150 points bonus awarded for sinking a ship.\n')
    print(
        '------------------------------- GAME INSTRUCTIONS --------' +
        '----------------------\n'
        )
    print('     Guess the co-ordinates of your opponents ship.')
    print('     Enter the co-ordinates and press Enter key to fire.')
    print('     Each torpedo fired on target is marked with " @ ".')
    print('     Each torpedo that is a miss is marked with " X ".')
    print('     To exit the game simply type exit into the input areas.')
    accept = input(
        '     When you are ready, press the enter key to continue \n     '
        )
    if accept == 'exit':
        end_game()
    print("     Great, it's time to obliterate your enemy")
    sleep(2)


def init_game_boards(user):
    """
    Function to create the game board and to call the
    functions to place the users and computers ships at
    random locations throughout the boards.
    """
    clear()
    global level
    if level == '1':
        for unused_variable_rowcol in range(0, 5):
            game_board.append([' . '] * 5)
            computers_game_board.append([' . '] * 5)
        init_ships(game_board)
        init_ships(computers_game_board)

    if level == '2':
        for unused_variable_rowcol in range(0, 7):
            game_board.append([' . '] * 7)
            computers_game_board.append([' . '] * 7)
        init_ships(game_board)
        init_ships(computers_game_board)

    if level == '3':
        for unused_variable_rowcol in range(0, 10):
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
    global users_score
    global computers_score
    if level == '1':
        
        column_nums = (
            '                 Columns:' +
            '1  2  3  4  5   | ' +
            ' 1  2  3  4  5'
            )
        space = ('                     ')
        spaces = ('    ')
        print(
            "------------------------------BRIANS BATTLESHIP GAME----" +
            "------------------------\n"
            )
        print(
            f'                Players score: {users_score}      ' +
            f'         Computers score: {computers_score}'
            )
        print()
        print(column_nums)
        print(
            '                     Rows                |' +
            '                Rows'
            )
        for num, rowcol in zip(range(0, 5), range(0, 5)):
            if num < 4:
                print(
                    space, num + 1, ''.join(game_board[rowcol]) + '  | ' +
                    ''.join(computers_game_board[rowcol]), num + 1
                    )
                num + 1
            else:
                print(
                    space, num + 1, ''.join(game_board[rowcol]) + '  | ' +
                    ''.join(computers_game_board[rowcol]), num + 1
                    )
        print()
        print(
            f"                {user}'s game board" + '\t\t' +
            "Computer's game board"
             )

    elif level == '2':
        
        column_nums = (
            '           Columns:' +
            '1  2  3  4  5  6  7   | ' +
            ' 1  2  3  4  5  6  7'
            )
        space = ('               ')
        spaces = ('    ')
        print(
            "------------------------------BRIANS BATTLESHIP GAME----" +
            "------------------------\n"
            )
        print(
            f'               Players score: {users_score}       ' +
            f'           Computers score: {computers_score}'
            )
        print(column_nums)
        print(
            '               Rows                      |' +
            '                      Rows'
            )
        for num, rowcol in zip(range(0, 7), range(0, 7)):
            if num < 6:
                print(
                    space, num + 1, ''.join(game_board[rowcol]) + '  | ' +
                    ''.join(computers_game_board[rowcol]), num + 1
                    )
                num + 1
            else:
                print(
                    space, num + 1, ''.join(game_board[rowcol]) + '  | ' +
                    ''.join(computers_game_board[rowcol]), num + 1
                    )
        print(
            f"             {user}'s game board" + '\t\t\t' +
            "Computer's game board"
            )
    elif level == '3':
        
        column_nums = (
            ' Columns:' +
            '1  2  3  4  5  6  7  8  9  10  | ' +
            ' 1  2  3  4  5  6  7  8  9  10'
            )
        space = ('     ')
        spaces = ('    ')
        print(
            "------------------------------BRIANS BATTLESHIP GAME----" +
            "------------------------\n"
            )
        print(
            f'         Players score: {users_score}                 ' +
            f' Computers score: {computers_score}'
            )
        print(column_nums)
        print(
            '     Rows                               |' +
            '                               Rows'
            )
        for num, rowcol in zip(range(0, 10), range(0, 10)):
            if num < 9:
                print(
                    space, num + 1, ''.join(game_board[rowcol]) + '  | ' +
                    ''.join(computers_game_board[rowcol]), num + 1
                    )
                num + 1
            else:
                print(
                    spaces, num + 1, ''.join(game_board[rowcol]) + '  | ' +
                    ''.join(computers_game_board[rowcol]), num + 1
                    )
        print(
            f"         {user}'s game board" + '\t\t\t' +
            "Computer's game board"
            )
    print()
    users_guess(user)


def random_row(game_board):
    """
    Function to return random row position within the game board
    to position ships
    """
    return randint(1, len(game_board[0]) - 1)


def random_col(game_board):
    """
    Function to return random column position within the game board
    to position ships
    """
    return randint(1, len(game_board[0]) - 1)


def random_orientation():
    """
    function to return random integer between 1 and 2 to
    determine the orientation of the ship on the game board
    """
    return randint(1, 2)


def init_ships(a_game_board):
    """
    Function to randomly place computers and players ships
     on a given game board,assign ship location to variable
     and store ship location in global variable
    """
    global level
    if a_game_board == game_board:
        if level == '1':
            user_ship1 = place_ship('<DD', a_game_board, used_rows, used_cols)
            location_of_ship('A', user_ship1)
            user_ship2 = place_ship('<DD', a_game_board, used_rows, used_cols)
            location_of_ship('B', user_ship2)
            user_ship3 = place_ship('<DD', a_game_board, used_rows, used_cols)
            location_of_ship('C', user_ship3)
        else:
            user_ship1 = place_ship('<DD', a_game_board, used_rows, used_cols)
            location_of_ship('A', user_ship1)
            user_ship2 = place_ship('<DD', a_game_board, used_rows, used_cols)
            location_of_ship('B', user_ship2)
            user_ship3 = place_ship('<DD', a_game_board, used_rows, used_cols)
            location_of_ship('C', user_ship3)
            user_ship4 = place_ship('<DD', a_game_board, used_rows, used_cols)
            location_of_ship('D', user_ship4)
    elif a_game_board == computers_game_board:
        if level == '1':
            computer_ship1 = place_ship(
                ' 1 ', a_game_board, used_rows, used_cols
                )
            location_of_ship('E', computer_ship1)
            computer_ship2 = place_ship(
                ' 2 ', a_game_board, used_rows, used_cols
                )
            location_of_ship('F', computer_ship2)
            computer_ship3 = place_ship(
                ' 3 ', a_game_board, used_rows, used_cols
                )
            location_of_ship('G', computer_ship3)
        else:
            computer_ship1 = place_ship(
                ' 1 ', a_game_board, used_rows, used_cols
                )
            location_of_ship('E', computer_ship1)
            computer_ship2 = place_ship(
                ' 2 ', a_game_board, used_rows, used_cols
                )
            location_of_ship('F', computer_ship2)
            computer_ship3 = place_ship(
                ' 3 ', a_game_board, used_rows, used_cols
                )
            location_of_ship('G', computer_ship3)
            computer_ship4 = place_ship(
                ' 4 ', a_game_board, used_rows, used_cols
                )
            location_of_ship('H', computer_ship4)


def pick_ship_coordinates(a_game_board):
    global ships_list
    global level   
        
    while True:
        ship_row = random_row(a_game_board)
        ship_col = random_col(a_game_board)        
        ship_row2 = ship_row + 1
        ship_col2 = ship_col + 1
        ship_marker = ship_row, ship_col
        ship = list(ship_marker)
        ship_marker_ = ship_row, ship_col2
        ship_ = list(ship_marker_)
        ship_marker2_ = ship_row2, ship_col
        ship2_ = list(ship_marker2_) 

        if level == '1':                
            if ship2_ not in ships_list:
                if ship_row < 2:
                    ship_row2 = ship_row + 1                         
                elif ship_row > 3:
                    ship_row2 = ship_row - 1
            if ship_ not in ships_list:
                if ship_col < 2:
                    ship_col2 = ship_col + 1
                elif ship_col > 3:
                    ship_col2 = ship_col - 1
            

        elif level == '2':
            if ship2_ not in ships_list:
                if ship_row < 2:
                    ship_row2 = ship_row + 1
                elif ship_row > 5:
                    ship_row2 = ship_row - 1
            if ship_ not in ships_list:
                if ship_col < 2:
                    ship_col2 = ship_col + 1
                elif ship_col > 5:
                    ship_col2 = ship_col - 1
            

        elif level == '3':
            if ship2_ not in ships_list:
                if ship_row < 2:
                    ship_row2 = ship_row + 1
                elif ship_row > 8:
                    ship_row2 = ship_row - 1
            if ship_ not in ships_list:
                if ship_col < 2:
                    ship_col2 = ship_col + 1
                elif ship_col > 8:
                    ship_col2 = ship_col - 1
            

        if ship not in ships_list:
            if ship_ not in ships_list:
                if ship2_ not in ships_list:
                    if ship and ship_ and ship2_ not in ships_list:
                        ship_data = ship_row, ship_col, ship_row2, ship_col2
                        return ship_data
    

def place_ship(char, a_game_board, used_rows, used_cols):
    global level    
    global ships_list

    while True:
        
        ship_data = pick_ship_coordinates(a_game_board)
        ship_row, ship_col, ship_row2, ship_col2 = ship_data        
        ship_marker = ship_row, ship_col
        ship = list(ship_marker)
        ship_marker_ = ship_row, ship_col2
        ship_ = list(ship_marker_)
        ship_marker2_ = ship_row2, ship_col
        ship2_ = list(ship_marker2_)      
            
        if ship not in ships_list:
            if ship_ not in ships_list:
                if ship2_ not in ships_list:
                    if ship and ship_ and ship2_ not in ships_list:
                        direction = random_orientation()                        
                        if a_game_board == game_board:
                            if direction == 1:
                                a_game_board[ship_row][ship_col] = '|$|'
                                a_game_board[ship_row2][ship_col] = '|$|' 
                                ships_list.append(ship)
                                ships_list.append(ship2_)                               
                                return ship, ship2_ 
                    
                            elif direction == 2:
                                a_game_board[ship_row][ship_col] = char
                                a_game_board[ship_row][ship_col2] = 'DD>'
                                ships_list.append(ship)
                                ships_list.append(ship_)                               
                                return ship, ship_  

                        elif a_game_board == computers_game_board:
                            if direction == 1:
                                a_game_board[ship_row][ship_col] = ' . '
                                a_game_board[ship_row][ship_col2] = ' . '
                                ships_list.append(ship)
                                ships_list.append(ship2_)    
                                return ship, ship2_
                    
                            elif direction == 2:
                                a_game_board[ship_row][ship_col] = ' . '
                                a_game_board[ship_row2][ship_col] = ' . '
                                ships_list.append(ship)
                                ships_list.append(ship_) 
                                return ship, ship_ 


def location_of_ship(ship, place):
    """
    Function to append the users and computers
    ship locations to a variable for the purpose
    of checking the ships positions in relation
    to the users guess. The use of global variables
    allows for the other functions in the program
    to access the variables once the data has been
    appended to the variables.
    """
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
    """
    Function to handle users guess input to the terminal and
    to check the guess is an integer and assign the guess to
    a variable, and to check if the guess has been previously
    guessed and act accordingly, also to initiate the computers
    guess and carry out the relevant tasks to continue the game
    or to finnish the game depending on conditions set out.
    """
    global bullets
    global computers_bullets
    global ships_list

    while bullets > 0:
        if user.lower() == 'brian':
            print(ship_A, ship_B, ship_C, ship_D)   # for testing purposes
            print(ship_E, ship_F, ship_G, ship_H)   # for testing purposes
            print(ships_list)
        print(
            f" {user}'s torpedoes: {bullets}/20          " +
            f" Computers torpedoes : {computers_bullets}/20"
            )
        print(
            f" {user}'s ships remaining:{users_ships_remaining}      " +
            "          " +
            f" Computers ships remaining: {computers_ships_remaining}"
            )
        while True:
            row = input(" Guess Row: ")
            guess_row = row
            num = check_num_input(guess_row)
            if num == 'True':
                guess_row = int(row)
                break

        while guess_row > 10:
            print(' Please enter a number from 1 to 10')
            while True:
                row = input(" Guess Row: ")
                guess_row = row
                num = check_num_input(guess_row)
                if num == 'True':
                    guess_row = int(row)
                    break
        while guess_row < 1:
            print(' Please enter a number from 1 to 10')
            while True:
                row = input(" Guess Row: ")
                guess_row = row
                num = check_num_input(guess_row)
                if num == 'True':
                    guess_row = int(row)
                    break

        while True:
            col = input(" Guess column: ")
            guess_col = col
            num = check_num_input(guess_col)
            if num == 'True':
                guess_col = int(col)
                break

        while guess_col > 10:
            print(' Please enter a number from 1 to 10')
            while True:
                col = input(" Guess column: ")
                guess_col = col
                num = check_num_input(guess_col)
                if num == 'True':
                    guess_col = int(col)
                    break
        while guess_col < 1:
            print(' Please enter a number from 1 to 10')
            while True:
                col = input(" Guess column: ")
                guess_col = col
                num = check_num_input(guess_col)
                if num == 'True':
                    guess_col = int(col)
                    break
        while True:
            guess = [guess_row, guess_col]
            if guess in users_used_guess:
                print(' You fired here before! Please try again:')
                while True:
                    row = input(" Guess Row: ")
                    guess_row = row
                    num = check_num_input(guess_row)
                    if num == 'True':
                        guess_row = int(row)
                        break

                while True:
                    col = input(" Guess column: ")
                    guess_col = col
                    num = check_num_input(guess_col)
                    if num == 'True':
                        guess_col = int(col)
                        break
            else:
                guess = [guess_row, guess_col]
                break

        users_used_guess.append(guess)
        print(f" {user} guessed row: {guess_row}, column: {guess_col}, {guess}")
        hit_or_miss = shots_fired(guess)
        print_board_char(hit_or_miss, guess_row, guess_col)
        bullets -= 1
        sleep(2)
        computers_guess()
        computers_bullets -= 1
        if bullets == 0:
            end_game()
        elif users_ships_remaining == 0:
            end_game()
        elif computers_ships_remaining == 0:
            end_game()
        else:
            sleep(3)
            clear()
            print_game_board(user)


def check_num_input(num_input):
    """
    Function to verify that the user input an
    integer as a value for targeting the computer
    and displays a message to the user displaying
    the character they input if not an integer
    """
    if num_input == 'exit':
        clear()
        end_game()

    try:
        unused_variable_num = int(num_input)
        return 'True'

    except ValueError:
        print(f' please enter a number value, you entered "{num_input}"')
        return 'False'


def computers_guess():
    """
    Function to choose random guess for the computer,
    and to check guess against the players ship locations
    to determine result.
    """
    guess_row = random_row(game_board)
    while guess_row > 10:
        guess_row = random_row(game_board)
    while guess_row < 1:
        guess_row = random_row(game_board)

    guess_col = random_col(game_board)
    while guess_col > 10:
        guess_col = random_col(game_board)
    while guess_col < 1:
        guess_col = random_col(game_board)

    computers_guess = guess_row, guess_col
    print(f' Computer guessed: {computers_guess}')
    hits = computers_shots_fired(computers_guess)
    print_board_char(hits, guess_row, guess_col)
    sleep(2)


def shots_fired(guess):
    """
    Function to check the players
    guess and to determine if the guess hit or
    missed the target and print the relevant message
    and increment the scores,depending on the data
    supplied when called.
    """
    global computers_ships_remaining
    global users_score
    hit = 'hit'
    miss = 'miss'
    if guess in ship_E:
        ship_E.remove(guess)
        if not ship_E:
            computers_ships_remaining -= 1
            print(
                ' Direct hit, ship sinking, computer only ' +
                f'has {computers_ships_remaining} ' +
                'battleships remaining'
                )
            users_score += 150
            print(' Bonus of 150 points awarded for sinking ship')
            sleep(2)
            return hit
        else:
            print(' Direct hit, computers ship defenses are down')
            return hit
    elif guess in ship_F:
        ship_F.remove(guess)
        if not ship_F:
            computers_ships_remaining -= 1
            print(
                ' Direct hit, ship sinking, computer only ' +
                f'has {computers_ships_remaining} ' +
                'battleships remaining'
                )
            users_score += 150
            print(" Bonus of 150 points awarded for sinking ship")
            sleep(2)
            return hit
        else:
            print(' Direct hit, computers ship defenses are down')
            return hit
    elif guess in ship_G:
        ship_G.remove(guess)
        if not ship_G:
            computers_ships_remaining -= 1
            print(
                ' Direct hit, ship sinking, computer only ' +
                f'has {computers_ships_remaining} ' +
                'battleships remaining'
                )
            users_score += 150
            print(" Bonus of 150 points awarded for sinking ship")
            sleep(2)
            return hit
        else:
            print(' Direct hit, computers ship defenses are down')
            return hit
    elif guess in ship_H:
        ship_H.remove(guess)
        if not ship_H:
            computers_ships_remaining -= 1
            print(
                ' Direct hit, ship sinking, computer only ' +
                f'has {computers_ships_remaining} ' +
                'battleships remaining'
                )
            users_score += 150
            print(" Bonus of 150 points awarded for sinking ship")
            sleep(2)
            return hit
        else:
            print(' Direct hit, computers ship defenses are down')
            return hit
    else:
        print(' You Missed')
        return miss


def computers_shots_fired(guess):
    """
    Function to check the computers
    guess and to determine if the guess hit or
    missed the target and print the relevant message
    and increment the scores,depending on the data
    supplied when called.
    """
    global users_ships_remaining
    global computers_score
    hit = 'hit_c'
    miss = 'miss_c'
    if guess in ship_A:
        ship_A.remove(guess)
        if not ship_A:
            users_ships_remaining -= 1
            print(
                ' Direct hit, ship sinking, player only ' +
                f'has {users_ships_remaining} ' +
                'battleships remaining'
                )
            computers_score += 150
            print(" Bonus of 150 points awarded for sinking ship")
            sleep(2)
            return hit
        else:
            print(' Direct hit, players ship defenses are down')
            return hit
    elif guess in ship_B:
        ship_B.remove(guess)
        if not ship_B:
            users_ships_remaining -= 1
            print(
                ' Direct hit, ship sinking, player only ' +
                f'has {users_ships_remaining} ' +
                'battleships remaining'
                )
            computers_score += 150
            print(" Bonus of 150 points awarded for sinking ship")
            sleep(2)
            return hit
        else:
            print(' Direct hit, players ship defenses are down')
            return hit
    elif guess in ship_C:
        ship_C.remove(guess)
        if not ship_C:
            users_ships_remaining -= 1
            print(
                ' Direct hit, ship sinking, player only ' +
                f'has {users_ships_remaining} ' +
                'battleships remaining'
                )
            computers_score += 150
            print(" Bonus of 150 points awarded for sinking ship")
            sleep(2)
            return hit
        else:
            print(' Direct hit, players ship defenses are down')
            return hit
    elif guess in ship_D:
        ship_D.remove(guess)
        if not ship_D:
            users_ships_remaining -= 1
            print(
                ' Direct hit, ship sinking, player only ' +
                f'has {users_ships_remaining} ' +
                'battleships remaining'
                )
            computers_score += 150
            print(" Bonus of 150 points awarded for sinking ship")
            sleep(2)
            return hit
        else:
            print(' Direct hit, players ship defenses are down')
            return hit
    else:
        print(' Computer Missed')
        return miss


def print_board_char(hit, guess_row, guess_col):
    """
    Function to increment scores and append the
    hit or miss locations to the relevant game
    boards, dependant on the data provided when
    called.
    """
    global users_score
    global computers_score
    if hit == 'hit':
        users_score += 300
        computers_game_board[guess_row - 1][guess_col - 1] = ' @ '
    elif hit == 'miss':
        computers_game_board[guess_row - 1][guess_col - 1] = ' X '
    elif hit == 'hit_c':
        computers_score += 300
        game_board[guess_row][guess_col] = ' @ '
    elif hit == 'miss_c':
        game_board[guess_row][guess_col] = ' X '


def clear():
    """
    Function to clear the terminal to keep playing
    area free from unused code,obtained from geeks for geeks.
    """
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def end_game():
    """
    Function to display scores and user message at
    end of game or on exiting, also prompting the user to play again.
    """
    clear()
    global user
    global users_score
    global computers_score
    global users_ships_remaining
    global computers_ships_remaining

    print(
        '---------------------------- BRIANS BATTLESHIP ' +
        'GAME ----------------------------\n'
        )
    print(
        f'      Congratulations {user} you ' +
        'have finnished Brians Battleship Game.'
        )
    print()
    print(
        '---------------------------------- GAME--' +
        'OVER ----------------------------------'
        )
    print()
    if users_score > computers_score:
        print(
            f'      You won the game with {users_score} points and ' +
            f'with {users_ships_remaining} ships still at sea.'
            )
        print(
            '      Thank you for playing my game, hope to ' +
            'see you again soon.'
            )
    elif users_score < computers_score:
        print(
            f'      Computer wins this time with {computers_score}' +
            f' points and {computers_ships_remaining} ships still sailing.'
            )
        print(
            f'      Thanks {user} for playing my game, better luck next time.'
            )
    print()
    high_scores()
    print()
    input('                  Press Enter key to restart game: \n')
    reset_var_data()
    main()


def high_scores():
    """
    Function to append the users name and score
    to the battleships google spreadsheet
    at the end of the game and to obtain the top
    5 high scores from the high scores google worksheet
    and print to console for the user to see.
    """
    global user
    global users_score

    new_row = user, users_score
    worksheet_to_update = SHEET.worksheet('players_scores')
    worksheet_to_update.append_row(new_row)
    print('                      Top 5 Highscore Leaderboard :')
    leaderboard = SHEET.worksheet('highscore').get_all_values()
    leaders = leaderboard[0:5]
    for leader in leaders:
        print('                         ', *leader)


def reset_var_data():
    """
    Function to reset all variable values at
    the end of each game, should the game be
    continued by the user at the end game screen.
    """
    global users_score
    users_score = 0
    global computers_score
    computers_score = 0
    global game_board
    game_board = []
    global computers_game_board
    computers_game_board = []
    global used_rows
    used_rows = []
    global used_cols
    used_cols = []
    global users_used_guess
    users_used_guess = []
    global computers_used_guess
    computers_used_guess = []
    global bullets
    bullets = 20
    global computers_bullets
    computers_bullets = 20
    global users_ships_remaining
    users_ships_remaining = 4
    global computers_ships_remaining
    computers_ships_remaining = 4
    global ship_A
    ship_A = []
    global ship_B
    ship_B = []
    global ship_C
    ship_C = []
    global ship_D
    ship_D = []
    global ship_E
    ship_E = []
    global ship_F
    ship_F = []
    global ship_G
    ship_G = []
    global ship_H
    ship_H = []


def main():
    """
    Function to run all game functions
    """
    username = welcome()
    game_rules()
    user = init_game_boards(username)
    print_game_board(user)


main()
