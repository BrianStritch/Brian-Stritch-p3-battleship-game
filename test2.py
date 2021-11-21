
def init_ships(a_game_board):
    """
    Function to randomly place computers and players ships
     on a given game board,assign ship location to variable
     and store ship location in global variable
    """
    global level
    if a_game_board == game_board:
        if level == '1':
            user_ship1 = place_ship('-DD', a_game_board, used_rows, used_cols)
            location_of_ship('A', user_ship1)
            user_ship2 = place_ship('-DD', a_game_board, used_rows, used_cols)
            location_of_ship('B', user_ship2)
            user_ship3 = place_ship('-DD', a_game_board, used_rows, used_cols)
            location_of_ship('C', user_ship3)
        else:
            user_ship1 = place_ship('-DD', a_game_board, used_rows, used_cols)
            location_of_ship('A', user_ship1)
            user_ship2 = place_ship('-DD', a_game_board, used_rows, used_cols)
            location_of_ship('B', user_ship2)
            user_ship3 = place_ship('-DD', a_game_board, used_rows, used_cols)
            location_of_ship('C', user_ship3)
            user_ship4 = place_ship('-DD', a_game_board, used_rows, used_cols)
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




def place_ship(char, a_game_board, used_rows, used_cols):
    """
    Function to select random position and assign to variable and place ship on
    position and append location to a list to be checked
     against to verify if location has been already selected and used.
    """
    global level
    global ship_A
    global ship_B
    global ship_C
    global ship_D
    global ship_E
    global ship_F
    global ship_G
    global ship_H

    while True:
        ship_row = random_row(a_game_board)
        if ship_row not in used_rows:
            used_rows.append(ship_row)
        else:
            ship_row = random_row(a_game_board)
            if ship_row not in used_rows:
                used_rows.append(ship_row)

        ship_col = random_col(a_game_board)
        if ship_col not in used_cols:
            used_cols.append(ship_col)
        else:
            ship_col = random_col(a_game_board)
            if ship_col not in used_rows:
                used_rows.append(ship_row)
        ship_col2 = ship_col + 1
        if ship_col2 not in used_cols:
            ship_col2 = ship_col + 1
            if level == '1':
                if ship_col2 > 4:
                    ship_col2 = ship_col - 1
                    used_cols.append(ship_col2)
                elif ship_col2 < 2:
                    ship_col2 = ship_col + 1
                    used_cols.append(ship_col2)
                else:
                    used_cols.append(ship_col2)
            if level == '2':
                if ship_col2 > 5:
                    ship_col2 = ship_col - 1
                    used_cols.append(ship_col2)
                else:
                    used_cols.append(ship_col2)
            if level == '3':
                if ship_col2 > 8:
                    ship_col2 = ship_col - 1
                    used_cols.append(ship_col2)
                else:
                    used_cols.append(ship_col2)
        else:
            used_cols.append(ship_col2)
        ship_row2 = ship_row + 1
        if ship_row2 not in used_rows:
            ship_row2 = ship_row + 1
            if level == '1':
                if ship_row2 > 4:
                    ship_row2 = ship_row - 1
                    used_rows.append(ship_row2)
                elif ship_row2 < 2:
                    ship_row2 = ship_col + 1
                    used_rows.append(ship_row2)
                else:
                    used_rows.append(ship_row2)
            if level == '2':
                if ship_row2 > 5:
                    ship_row2 = ship_col - 1
                    used_rows.append(ship_row2)
                else:
                    used_rows.append(ship_row2)
            if level == '3':
                if ship_row2 > 8:
                    ship_row2 = ship_col - 1
                    used_rows.append(ship_row2)
                else:
                    used_rows.append(ship_row2)
        else:
            used_rows.append(ship_row2)
        direction = random_orientation()
        if a_game_board == game_board:
            if direction == 1:
                a_game_board[ship_row][ship_col] = '|$|'
                a_game_board[ship_row2][ship_col] = '|$|'
                ship = ship_row, ship_col
                ship_ = ship_row2, ship_col
                return ship, ship_
            elif direction == 2:
                a_game_board[ship_row][ship_col] = char
                a_game_board[ship_row][ship_col2] = char
                ship = ship_row, ship_col
                ship_ = ship_row, ship_col2
                return ship, ship_

        if a_game_board == computers_game_board:
            if direction == 1:
                a_game_board[ship_row][ship_col] = " . "
                a_game_board[ship_row][ship_col2] = " . "
                ship = ship_row, ship_col
                ship_ = ship_row, ship_col2            
                return ship, ship_
            elif direction == 2:
                a_game_board[ship_row][ship_col] = " . "
                a_game_board[ship_row2][ship_col] = " . "
                ship = ship_row, ship_col
                ship_ = ship_row2, ship_col
                return ship, ship_

def print_board_char(x,y):
    ships = list


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
    


def place_ship(char, a_game_board, used_rows, used_cols):
    global level
    global ship_A
    global ship_B
    global ship_C
    global ship_D
    global ship_E
    global ship_F
    global ship_G
    global ship_H
    ships_list = ship_A, ship_B, ship_C, ship_D, ship_E, ship_F, ship_G, ship_H
    ship1 = ()
    ship2 = ()

    while True:
        ship_row = random_row(a_game_board)
        ship_col = random_col(a_game_board)
        
        if level == '1':
            if ship_row < 2:
                ship_row2 = ship_row + 1
            elif ship_row > 4:
                ship_row2 = ship_row - 1
            elif ship_col < 2:
                ship_col2 = ship_col + 1
            elif ship_row > 4:
                ship_col2 = ship_col - 1

        elif level == '2':
            if ship_row < 2:
                ship_row2 = ship_row + 1
            elif ship_row > 6:
                ship_row2 = ship_row - 1
            elif ship_col < 2:
                ship_col2 = ship_col + 1
            elif ship_row > 6:
                ship_col2 = ship_col - 1
        elif level == '3':
            if ship_row < 2:
                ship_row2 = ship_row + 1
            elif ship_row > 9:
                ship_row2 = ship_row - 1
            elif ship_col < 2:
                ship_col2 = ship_col + 1
            elif ship_row > 9:
                ship_col2 = ship_col - 1
        
            
            

        ship_col2 = ship_col + 1
        
        ship = ship_row, ship_col
        ship_ = ship_row, ship_col2
        ship2_ = ship_row2, ship_col
        direction = random_orientation() 
        

        if ship or ship_ or ship2_ not in ships_list:
            if a_game_board == game_board:
                if direction == 1:
                    a_game_board[ship_row][ship_col] = '|$|'
                    a_game_board[ship_row2][ship_col] = '|$|'
                    ship1 = ship
                    ship2 = ship2
                    break
                    
                elif direction == 2:
                    a_game_board[ship_row][ship_col] = char
                    a_game_board[ship_row][ship_col2] = char
                    ship1 = ship
                    ship2 = ship2
                    break
                   

            if a_game_board == computers_game_board:
                if direction == 1:
                    a_game_board[ship_row][ship_col] = " . "
                    a_game_board[ship_row][ship_col2] = " . "   
                    ship1 = ship
                    ship2 = ship2 
                    break     
                    
                elif direction == 2:
                    a_game_board[ship_row][ship_col] = " . "
                    a_game_board[ship_row2][ship_col] = " . "
                    ship1 = ship
                    ship2 = ship2
                    break 
    return ship1, ship2       




    










        if ship_row not in used_rows:
            used_rows.append(ship_row)
        else:
            ship_row = random_row(a_game_board)
            if ship_row not in used_rows:
                used_rows.append(ship_row)

        
        if ship_col not in used_cols:
            used_cols.append(ship_col)
        else:
            ship_col = random_col(a_game_board)
            if ship_col not in used_rows:
                used_rows.append(ship_row)
        
        if ship_col2 not in used_cols:
            ship_col2 = ship_col + 1
            if level == '1':
                if ship_col2 > 4:
                    ship_col2 = ship_col - 1
                    used_cols.append(ship_col2)
                elif ship_col2 < 2:
                    ship_col2 = ship_col + 1
                    used_cols.append(ship_col2)
                else:
                    used_cols.append(ship_col2)
            if level == '2':
                if ship_col2 > 5:
                    ship_col2 = ship_col - 1
                    used_cols.append(ship_col2)
                else:
                    used_cols.append(ship_col2)
            if level == '3':
                if ship_col2 > 8:
                    ship_col2 = ship_col - 1
                    used_cols.append(ship_col2)
                else:
                    used_cols.append(ship_col2)
        else:
            used_cols.append(ship_col2)
        
        if ship_row2 not in used_rows:
            ship_row2 = ship_row + 1
            if level == '1':
                if ship_row2 > 4:
                    ship_row2 = ship_row - 1
                    used_rows.append(ship_row2)
                elif ship_row2 < 2:
                    ship_row2 = ship_col + 1
                    used_rows.append(ship_row2)
                else:
                    used_rows.append(ship_row2)
            if level == '2':
                if ship_row2 > 5:
                    ship_row2 = ship_col - 1
                    used_rows.append(ship_row2)
                else:
                    used_rows.append(ship_row2)
            if level == '3':
                if ship_row2 > 8:
                    ship_row2 = ship_col - 1
                    used_rows.append(ship_row2)
                else:
                    used_rows.append(ship_row2)
        else:
            used_rows.append(ship_row2)