from random import randint


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


game_board = []


def player_game_board(user):
    """
    Function to create game board 10 units by 10 units for player.
    """
    for rowcol in range(0, 10):
        game_board.append([' . '] * 10)
    print()
    player_ships(game_board)
    for row in game_board:
        print(''.join(row))
    print(f"{user}'s game board")

    return game_board


def computer_game_board():
    """
    Function to create game board 10 units by 10 units for computer.
    """
    computer_game_board = []
    for rowcol in range(0, 10):
        computer_game_board.append([' . '] * 10)
    print()
    for row in computer_game_board:
        print(''.join(row))
    print("Computer's game board")


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


def player_ships(game_board):
    """
    Function to randomly place players ships on game board
    """
    used_row = []
    used_col = []

    ship1_row = random_row(game_board)
    used_row.append(ship1_row)
    ship1_col = random_col(game_board)
    used_col.append(ship1_col)
    ship1_col2 = ship1_col + 1
    used_col.append(ship1_col2)
    game_board[ship1_row][ship1_col] = " X "
    game_board[ship1_row][ship1_col2] = " X "

    ship2_row = random_row(game_board)
    if ship2_row not in used_row:
        used_row.append(ship2_row)
    ship2_col = random_col(game_board)
    if ship2_col not in used_col:
        used_col.append(ship2_col)
    ship2_row2 = ship2_row + 1
    if ship2_row2 not in used_col:
        used_col.append(ship2_row2)
    game_board[ship2_row][ship2_col] = " X "
    game_board[ship2_row2][ship2_col] = " X "

    ship3_row = random_row(game_board)
    if ship3_row not in used_row:
        used_row.append(ship3_row)
    ship3_col = random_col(game_board)
    if ship3_col not in used_col:
        used_col.append(ship3_col)
    ship3_row2 = ship3_row + 1
    if ship3_row2 not in used_col:
        used_col.append(ship3_row2)
    game_board[ship3_row][ship3_col] = " X "
    game_board[ship3_row2][ship3_col] = " X "

    ship4_row = random_row(game_board)
    if ship4_row not in used_row:
        used_row.append(ship4_row)
    ship4_col = random_col(game_board)
    if ship4_col not in used_col:
        used_col.append(ship4_col)
    ship4_col2 = ship4_col + 1
    if ship4_col2 not in used_col:
        used_col.append(ship4_col2)
    game_board[ship4_row][ship4_col] = " X "
    game_board[ship4_row][ship4_col2] = " X "


def main():
    """
    Function to run all game functions
    """
    username = welcome()
    player_game_board(username)
    computer_game_board()


main()
