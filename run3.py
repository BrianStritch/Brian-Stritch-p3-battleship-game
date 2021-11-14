from random import randint
# import only system from os
from os import system, name
# import sleep to show output for some time period
from time import sleep

user = ''
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


def welcome():
    """
    function to clear the console, then to get the Username from the
    user and issue welcome message.
    """
    global user
    clear()
    print()
    print('------------------------------- Welcome to ----------------------------------\n')
    print("---------------------------BRIANS BATTLESHIP GAME----------------------------\n")
    print('-----------------------------------------------------------------------------')
    user_name = input('     Enter your name here:\n')
    user = user_name.capitalize()
    if user == 'exit':
        end_game()
    print(f"     Welcome {user}, good luck, you'll need it")
    return user


def game_rules():
    """
    Function to display the game description and instructions prior to the game starting.
    """
    sleep(1)
    clear()
    print("---------------------------BRIANS BATTLESHIP GAME----------------------------\n")
    print('     Players get 4 ships each.')
    print('     Each ship is 2 characters wide.')
    print('     Each Player gets 20 torpedos.')
    print('     Player goes first, then its the computers turn.')
    print('     Each player gets 300 points per target hit.')
    print('     Additional 150 points bonus awarded for sinking a ship.\n')
    print('-------------------------GAME INSTRUCTIONS---------------------\n')
    print('     Guess the co-ordinates of your opponents ship.')
    print('     Top left corner is row: 1, column: 1.')
    print('     Enter the co-ordinates and press Enter key to fire.')
    print('     Each torpedo fired on target is marked with " @ ".')
    print('     Each torpedo that is a miss is marked with " X ".')
    print('     To exit the game simply type exit into the input areas.')
    accept = input('     When you are ready, press the enter key to continue \n     ')
    if accept == 'exit':
        end_game()
    print("     Great, it's time to obliterate your enemy")
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
    nums = ('Columns: 1  2  3  4  5  6  7  8  9  10  |  1  2  3  4  5  6  7  8  9  10')
    space = ('     ')
    spaces = ('    ')
    global users_score
    global computers_score
    print("---------------------------BRIANS BATTLESHIP GAME----------------------------\n")
    print(f'         Players score: {users_score}                  Computers score: {computers_score}')
    print(nums)
    print('     Rows                               |                              Rows')
    for num, rowcol in zip(range(0, 10), range(0, 10)):
        if num < 9:
            print(
               space, num + 1, ''.join(game_board[rowcol]) + '  | ' + ''.join(computers_game_board[rowcol]), num + 1
                )
            num + 1
        else:
            print(
                spaces, num + 1, ''.join(game_board[rowcol]) + '  | ' + ''.join(computers_game_board[rowcol]), num + 1
                )
    print(f"         {user}'s game board" + '\t\t\t' + "Computer's game board")
    print()
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
        user_ship2 = place_ship('-DD', a_game_board, used_rows, used_cols)
        location_of_ship('B', user_ship2)
        user_ship3 = place_ship('-DD', a_game_board, used_rows, used_cols)
        location_of_ship('C', user_ship3)
        user_ship4 = place_ship('-DD', a_game_board, used_rows, used_cols)
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
    """
    Function to select random position and assign to variable and place ship on
    position and append location to a list to be checked
     against to verify if location has been already selected and used.
    """
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
        a_game_board[ship_row][ship_col] = " . "
        a_game_board[ship_row][ship_col2] = " . "
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
    global computers_bullets
    while bullets > 0:
        print(ship_E, ship_F, ship_G, ship_H)
        print(f"{user}'s torpedo's remaining: {bullets}          Computers remaining torpedos: {computers_bullets}")
        print(f"{user}'s ships remaining:{users_ships_remaining}                 Computers ships remaining: {computers_ships_remaining}")
        while True:
            row = input("Guess Row: ")
            guess_row = row
            num = check_num_input(guess_row)
            if num == True:
                guess_row = int(row)
                break
            
        while True:
            col = input("Guess column: ")
            guess_col = col
            num = check_num_input(guess_col)
            if num == True:
                guess_col = int(col)
                break

        while guess_row > 10:
            print('Please enter a number from 1 to 10')
            while True:
                row = input("Guess Row: ")
                guess_row = row
                num = check_num_input(guess_row)
                if num == True:
                    guess_row = int(row)
                    break

        while guess_col > 10:
            print('Please enter a number from 1 to 10')
            while True:
                col = input("Guess column: ")
                guess_col = col
                num = check_num_input(guess_col)
                if num == True:
                    guess_col = int(col)
                    break

        guess = (guess_row, guess_col)
        if guess in users_used_guess:
            print('you fired here before! Please try again:')
            while True:
                row = input("Guess Row: ")
                guess_row = row
                num = check_num_input(guess_row)
                if num == True:
                    guess_row = int(row)
                    break

            while True:
                col = input("Guess column: ")
                guess_col = col
                num = check_num_input(guess_col)
                if num == True:
                    guess_col = int(col)
                    break

        users_used_guess.append(guess)
        print(f"{user} guessed row: {guess_row}, column: {guess_col}")
        hit_or_miss = shots_fired(guess)
        print_board_char(hit_or_miss, guess_row, guess_col)
        bullets -= 1
        sleep(1)
        computers_guess()
        computers_bullets -= 1
        if bullets == 0:
            end_game()
        elif users_ships_remaining == 0:
            end_game()
        elif computers_ships_remaining == 0:
            end_game()
        else:
            sleep(2)
            clear()
            print_game_board(user)


def check_num_input(num_input):
    """
    Function to verify that the user input an
    integer as a value for targeting the computer
    and displays a message to the user displaying
    the charachter they input if not an integer
    """
    print(num_input)
    sleep(1)
    
    if num_input == 'exit':
        clear()
        end_game()   
   
    try:
        num = int(num_input)
        return True

    except ValueError:
        print(f"please enter a number value, you entered {num_input}.")
        return False


def computers_guess():
    guess_row = random_row(game_board)
    guess_col = random_col(game_board)
    computers_guess = guess_row, guess_col
    print(f'Computer guessed: {computers_guess}')
    hits = computers_shots_fired(computers_guess)
    print_board_char(hits, guess_row, guess_col)
    sleep(1)


def shots_fired(guess):
    global computers_ships_remaining
    global users_score
    hit = 'hit'
    miss = 'miss'
    if guess in ship_E:
        ship_E.remove(guess)
        if not ship_E:
            computers_ships_remaining -= 1
            print(f'Direct hit, ship sinking, computer only has {computers_ships_remaining} battleships remaining')
            users_score += 150
            print('Bonus of 150 points awarded for sinking ship')
            sleep(1)
            return hit
        else:
            print('Direct hit, computers ship defenses are down')
            return hit
    elif guess in ship_F:
        ship_F.remove(guess)
        if not ship_F:
            computers_ships_remaining -= 1
            print(f'Direct hit, ship sinking, computer only has {computers_ships_remaining} battleships remaining')
            users_score += 150
            print("Bonus of 150 points awarded for sinking ship")
            sleep(1)
            return hit
        else:
            print('Direct hit, computers ship defenses are down')
            return hit
    elif guess in ship_G:
        ship_G.remove(guess)
        if not ship_G:
            computers_ships_remaining -= 1
            print(f'Direct hit, ship sinking, computer only has {computers_ships_remaining} battleships remaining')
            users_score += 150
            print("Bonus of 150 points awarded for sinking ship")
            sleep(1)
            return hit
        else:
            print('Direct hit, computers ship defenses are down')
            return hit
    elif guess in ship_H:
        ship_H.remove(guess)
        if not ship_H:
            computers_ships_remaining -= 1
            print(f'Direct hit, ship sinking, computer only has {computers_ships_remaining} battleships remaining')
            users_score += 150
            print("Bonus of 150 points awarded for sinking ship")
            sleep(1)
            return hit
        else:
            print('Direct hit, computers ship defenses are down')
            return hit
    else:
        print('You Missed')
        return miss


def computers_shots_fired(guess):
    global users_ships_remaining
    global computers_score
    hit = 'hit_c'
    miss = 'miss_c'
    if guess in ship_A:
        ship_A.remove(guess)
        if not ship_A:
            users_ships_remaining -= 1
            print(f'Direct hit, ship sinking, player only has {users_ships_remaining} battleships remaining')
            computers_score += 150
            print("Bonus of 150 points awarded for sinking ship")
            sleep(1)
            return hit
        else:
            print('Direct hit, players ship defenses are down')
            return hit
    elif guess in ship_B:
        ship_B.remove(guess)
        if not ship_B:
            users_ships_remaining -= 1
            print(f'Direct hit, ship sinking, player only has {users_ships_remaining} battleships remaining')
            computers_score += 150
            print("Bonus of 150 points awarded for sinking ship")
            sleep(1)
            return hit
        else:
            print('Direct hit, players ship defenses are down')
            return hit
    elif guess in ship_C:
        ship_C.remove(guess)
        if not ship_C:
            users_ships_remaining -= 1
            print(f'Direct hit, ship sinking, player only has {users_ships_remaining} battleships remaining')
            computers_score += 150
            print("Bonus of 150 points awarded for sinking ship")
            sleep(1)
            return hit
        else:
            print('Direct hit, players ship defenses are down')
            return hit
    elif guess in ship_D:
        ship_D.remove(guess)
        if not ship_D:
            users_ships_remaining -= 1
            print(f'Direct hit, ship sinking, player only has {users_ships_remaining} battleships remaining')
            computers_score += 150
            print("Bonus of 150 points awarded for sinking ship")
            sleep(1)
            return hit
        else:
            print('Direct hit, players ship defenses are down')
            return hit
    else:
        print('Computer Missed')
        return miss


def print_board_char(hit, guess_row, guess_col):
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
    
    global users_score
    global computers_score
    global users_ships_remaining
    global computers_ships_remaining
    global user
    print("-----------------------BRIANS BATTLESHIP GAME-------------------\n")
    print('----------------------------GAME OVER! -------------------------')
    print()
    if users_ships_remaining > computers_ships_remaining:
        print(
            f"Congratulations {user} you won the game with {users_score} points and {users_ships_remaining} ships remaining."
            
        )
        print(
            f'The computer had {computers_ships_remaining} ships remaining, and had {computers_score} points at the end of the game.'
        )
        print('Thank you for playing my game, hope to see you again soon.')
        print()
        play_again()

    elif users_score < computers_score:
        print(f'Computer wins this time with {computers_score} points, and {computers_ships_remaining} ships remaining.')
        print(f'Thanks {user} for playing my game, better luck next time.')
        play_again()
        
    elif users_ships_remaining < computers_ships_remaining:
        print(f'Computer wins this time with {computers_score} points, and {computers_ships_remaining} ships remaining.')        
        print(
            f'The computer had {computers_ships_remaining} ships remaining, and had {computers_score} points at the end of the game.'
        )
        print('Thank you for playing my game, hope to see you again soon.')
        print()
        # play_again()
        play_again = input('     Would you like to play again? Y/N :  \n')	
        if play_again.lower() == 'y':	
            reset_var_data()	
            main()

def play_again():
    play_again = input('Would you like to play again? Y/N :  \n')
    if play_again.lower() == 'y':
        reset_var_data()
        main()
    else:
        print('-----------------------BRIANS BATTLESHIP GAME-------------------')
        print('--------------------------- GAME OVER --------------------------')
        exit()
  

def reset_var_data():
    """
    Function to reset all variable values at the end of each game
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