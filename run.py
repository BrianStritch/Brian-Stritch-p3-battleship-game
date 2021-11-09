from random import randint


def welcome():
    """
    get Username from the user
    """
    print()
    print('------------------------------')
    print("Welcome to Brian's battleship game.")
    print('------------------------------')
    user = input('Enter your name here:\n')
    print(f"Welcome {user}, good luck, you'll need it")
    return user


def player_game_board(user):
    """
    Function to create game board 10 units by 10 units for player.
    """
    game_board = []
    for rowcol in range(0, 10):
        game_board.append([' . '] * 10)
    print()
    for row in game_board:
        print(''.join(row))
    print(f"{user}'s game board")


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


def main():
    username = welcome()    
    player_game_board(username)
    computer_game_board()


main()
