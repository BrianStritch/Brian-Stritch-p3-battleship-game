
    # elif computer_hit == 3:
    #     while True:
    #         if level == '1':
    #             computer_guess_hit = [computer_guess_row , computer_guess_col - 1]            
    #             if computer_guess_hit not in computers_used_guess and computer_guess_col >= 4:
    #                 break
    #             elif computer_guess_hit not in computers_used_guess and computer_guess_col <= 0:
    #                 computer_guess_hit = [computer_guess_row , computer_guess_col + 1]
    #                 break
    #             elif computer_guess_hit not in computers_used_guess and computer_guess_col >= 4:
    #                 computer_guess_hit = [computer_guess_row - 1, computer_guess_col]
    #                 break
    #             elif computer_guess_hit not in computers_used_guess and computer_guess_col <= 0:
    #                 computer_guess_hit = [computer_guess_row + 1, computer_guess_col]
    #                 break
    #         if level == '2':
    #             computer_guess_hit = [computer_guess_row , computer_guess_col - 1]
    #             if computer_guess_hit not in computers_used_guess and computer_guess_col >= 6:                    
    #                 break
    #             elif computer_guess_hit not in computers_used_guess and computer_guess_col <= 0:
    #                 computer_guess_hit = [computer_guess_row , computer_guess_col + 1]
    #                 break
    #             elif computer_guess_hit not in computers_used_guess and computer_guess_col >= 6:
    #                 computer_guess_hit = [computer_guess_row - 1, computer_guess_col]
    #                 break
    #             elif computer_guess_hit not in computers_used_guess and computer_guess_col >= 0:
    #                 computer_guess_hit = [computer_guess_row + 1, computer_guess_col]
    #                 break

    #         if level == '3':
    #             computer_guess_hit = [computer_guess_row , computer_guess_col - 1]
    #             if computer_guess_hit not in computers_used_guess and computer_guess_col >= 9:                    
    #                 break
    #             elif computer_guess_hit not in computers_used_guess and computer_guess_col <= 0:
    #                 computer_guess_hit = [computer_guess_row , computer_guess_col - 1]
    #                 break
    #             elif computer_guess_hit not in computers_used_guess and computer_guess_col >= 9:
    #                 computer_guess_hit = [computer_guess_row - 1, computer_guess_col]
    #                 break
    #             elif computer_guess_hit not in computers_used_guess and computer_guess_col <= 0:
    #                 computer_guess_hit = [computer_guess_row + 1, computer_guess_col]
    #                 break







    # elif computer_hit == 3:
    #     while True:    
    #         if level == '2':
    #             computer_guess_hit = [computer_guess_row , computer_guess_col + 1]            
    #             if computer_guess_hit not in computers_used_guess and computer_guess_col <= 0:
    #                 break
    #             elif computer_guess_hit not in computers_used_guess and computer_guess_col >= 4:
    #                 computer_guess_hit = [computer_guess_row , computer_guess_col - 1]
    #                 break
    #             elif computer_guess_hit not in computers_used_guess and computer_guess_col >= 4:
    #                 computer_guess_hit = [computer_guess_row - 1, computer_guess_col]
    #                 break
    #             elif computer_guess_hit not in computers_used_guess and computer_guess_col <= 0:
    #                 computer_guess_hit = [computer_guess_row + 1, computer_guess_col]
    #                 break







            








        # if True:
        #     
        #         while True:
        #             if computer_guess_col >= 4:
        #                 computer_guess_hit = [computer_guess_row , computer_guess_col - 1]
        #                 if computer_guess_hit not in computers_used_guess:
        #                     break
        #                 elif computer_guess_col >= 0:                            
        #                     computer_guess_hit = [computer_guess_row, computer_guess_col + 1]
        #                     if computer_guess_hit not in computers_used_guess:
        #                         break
        #             else:
        #                 computer_guess_hit = [computer_guess_row, computer_guess_col + 1]
        #                 break 
            
        #     elif computer_hit_attempt == 2:
        #         if computer_guess_col >= 4:
        #             computer_guess_hit = [computer_guess_row , computer_guess_col - 1]
        #         elif computer_guess_col >= 0: 
        #             computer_guess_hit = [computer_guess_row, computer_guess_col + 1]
        #         else:
        #             computer_guess_hit = [computer_guess_row, computer_guess_col - 1]
                

        #     elif computer_hit_attempt == 3:
        #         if computer_guess_row >= 4:
        #             computer_guess_hit = [computer_guess_row - 1, computer_guess_col]
        #         elif computer_guess_row <= 0: 
        #             computer_guess_hit = [computer_guess_row + 1, computer_guess_col]
        #         else:
        #             computer_guess_hit = [computer_guess_row + 1, computer_guess_col]
            
        #     elif computer_hit_attempt == 4:
        #         if computer_guess_row >= 4:
        #             computer_guess_hit = [computer_guess_row - 1, computer_guess_col]
        #         elif computer_guess_row <= 0: 
        #             computer_guess_hit = [computer_guess_row + 1, computer_guess_col]
        #         else:
        #             computer_guess_hit = [computer_guess_row - 1, computer_guess_col]







""" this code works but allows the computer
to keep reselecting previously selected places
"""
        
def computers_guess():
    """
    Function to choose random guess for the computer,
    and to check guess against the players ship locations
    to determine result. Additional functionality to
     behave like AI if shots fired on target.
    """
    global computer_hit_col
    global computer_hit_row
    global computer_hit_attempt
    global computer_hit
    global computer_guess_hit
    global computer_guess_row
    global computer_guess_col

    if computer_hit == 1:
        computer_guess_row = random_row(game_board)
        while computer_guess_row > 10:
            computer_guess_row = random_row(game_board)
        while computer_guess_row < 1:
            computer_guess_row = random_row(game_board)

        computer_guess_col = random_col(game_board)
        while computer_guess_col > 10:
            computer_guess_col = random_col(game_board)
        while computer_guess_col < 1:
            computer_guess_col = random_col(game_board)

        computers_guess = [computer_guess_row, computer_guess_col]
        computer_hit_row = computer_guess_row
        computer_hit_col = computer_guess_col
        print(f' Computer guessed: {computers_guess}')
        hits = computers_shots_fired(computers_guess)
        print_board_char(hits, computer_guess_row, computer_guess_col)
        sleep(2)
    
    elif computer_hit == 2:
        if True:
            if computer_hit_attempt == 1:
                computer_guess_hit = [computer_guess_row, computer_guess_col + 1]

            elif computer_hit_attempt == 2:
                computer_guess_hit = [computer_guess_row, computer_guess_col - 1]

            elif computer_hit_attempt == 3:
                computer_guess_hit = [computer_guess_row + 1, computer_guess_col]
            
            elif computer_hit_attempt == 4:
                computer_guess_hit = [computer_guess_row - 1, computer_guess_col]
        
        print(f' Computer guessed: {computer_guess_hit}')
        hits = computers_shots_fired(computer_guess_hit)
        x,y = computer_guess_hit
        print_board_char(hits, x , y )
        sleep(2)


"""
    this one has good logic if i can get it to work
"""




def computers_guess():
    """
    Function to choose random guess for the computer,
    and to check guess against the players ship locations
    to determine result. Additional functionality to
     behave like AI if shots fired on target.
    """
    global computer_hit_col
    global computer_hit_row
    global computer_hit_attempt
    global computer_hit
    global computer_guess_hit
    global computer_guess_row
    global computer_guess_col
    global computers_used_guess

    if computer_hit == 1:
        computer_guess_row = int(random_row(game_board))
        while computer_guess_row > 10:
            computer_guess_row = int(random_row(game_board))
        while computer_guess_row < 1:
            computer_guess_row = int(random_row(game_board))
        computer_guess_col = int(random_col(game_board))
        while computer_guess_col > 10:
            computer_guess_col = int(random_col(game_board))
        while computer_guess_col < 1:
            computer_guess_col = int(random_col(game_board))
        while True:
            computers_guess = [computer_guess_row, computer_guess_col]
            if computers_guess in computers_used_guess:
                computer_guess_row = int(random_row(game_board))
                while computer_guess_row > 10:
                    computer_guess_row = int(random_row(game_board))
                while computer_guess_row < 1:
                    computer_guess_row = int(random_row(game_board))
            else:
                computers_guess = [computer_guess_row, computer_guess_col]
                break   
     
        computers_used_guess.append(computers_guess)
        computers_guess = [computer_guess_row, computer_guess_col]
        computers_guess_display = [computer_guess_row + 1, computer_guess_col + 1]
        computer_hit_row = computer_guess_row
        computer_hit_col = computer_guess_col
        print(f' Computer guessed: {computers_guess_display}')
        hits = computers_shots_fired(computers_guess)
        print_board_char(hits, computer_guess_row, computer_guess_col)
        sleep(2)
    
    elif computer_hit == 2:
        while True:
            if level == '1':
                computer_guess_hit = [computer_guess_row , computer_guess_col - 1]            
                if computer_guess_col >= 5 and computer_guess_hit not in computers_used_guess:
                    break
                elif computers_guess_col <= 0 and computer_guess_hit not in computers_used_guess:
                    computer_guess_hit = [computer_guess_row , computer_guess_col + 1]
                    break
                elif computers_guess_row >= 5 and computer_guess_hit not in computers_used_guess:
                    computer_guess_hit = [computer_guess_row - 1, computer_guess_col]
                    break
                elif computers_guess_row <= 0 and computer_guess_hit not in computers_used_guess:
                    computer_guess_hit = [computer_guess_row + 1, computer_guess_col]
                    break
                  

            elif level == '2':
                computer_guess_hit = [computer_guess_row , computer_guess_col - 1]            
                if computer_guess_col >= 7 and computer_guess_hit not in computers_used_guess:
                    break
                elif computers_guess_col <= 0 and computer_guess_hit not in computers_used_guess:
                    computer_guess_hit = [computer_guess_row , computer_guess_col + 1]
                    break
                elif computers_guess_row >= 7 and computer_guess_hit not in computers_used_guess:
                    computer_guess_hit = [computer_guess_row - 1, computer_guess_col]
                    break
                elif computers_guess_row <= 0 and computer_guess_hit not in computers_used_guess:
                    computer_guess_hit = [computer_guess_row + 1, computer_guess_col]
                    break
                
                
            elif level == '3':
                computer_guess_hit = [computer_guess_row , computer_guess_col - 1]            
                if computer_guess_col >= 10 and computer_guess_hit not in computers_used_guess:
                    break
                elif computers_guess_col <= 0 and computer_guess_hit not in computers_used_guess:
                    computer_guess_hit = [computer_guess_row , computer_guess_col + 1]
                    break
                elif computers_guess_row >= 10 and computer_guess_hit not in computers_used_guess:
                    computer_guess_hit = [computer_guess_row - 1, computer_guess_col]
                    break
                elif computers_guess_row <= 0 and computer_guess_hit not in computers_used_guess:
                    computer_guess_hit = [computer_guess_row + 1, computer_guess_col]
                    break
                 

            
        x,y = computer_guess_hit            
        computers_guess_display_hit = [x + 1, y + 1]
        print(f' Computer guessed: {computers_guess_display_hit}')        
        hits = computers_shots_fired(computer_guess_hit)
        computers_used_guess.append(computer_guess_hit)
        x,y = computer_guess_hit
        print_board_char(hits, x , y )
        sleep(2)























elif computer_hit == 2:
        while True:
            if computer_hit_attempt == 1:
                computer_guess_hit = [computer_guess_row, computer_guess_col + 1]
                
            elif computer_hit_attempt == 2:
                computer_guess_hit = [computer_guess_row, computer_guess_col - 1]

            elif computer_hit_attempt == 3:
                computer_guess_hit = [computer_guess_row + 1, computer_guess_col]
            
            elif computer_hit_attempt == 4:
                computer_guess_hit = [computer_guess_row - 1, computer_guess_col]