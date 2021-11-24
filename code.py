
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