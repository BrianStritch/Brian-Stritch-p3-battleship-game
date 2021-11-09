from random import randint


def player_game_board():
    """
    Function to create game board 10 units by 10 units.
    """
    game_board = []
    for rowcol in range(0, 10):
        game_board.append([' . '] * 10)
    print()
    for row in game_board:
        print(''.join(row))
    print()


player_game_board()
