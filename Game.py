import Board        #imports my file containing the game board
import Enemy_Ai     #imports the enemy AI


game            = Board.Tictactoe() #create instance of the board                 #set a default end condition to make players take turns until one of them wins
opponent        = Enemy_Ai.Enemy()        #create instance of opponent

while(game.condition == 0):
    game.display_key()
    print("Please enter the number of the position you would like to place an X in.")
    valid = 0

    while(valid == 0):
        chosen_position = int(input())
        if(chosen_position > len(game.board) or chosen_position < 0):
            print("Sorry, that position doesn't exist. Please try again.")
        elif(game.board[chosen_position] == 1):
            print("You have already placed an X in that position. Please try another position")
        elif(game.board[chosen_position] == 2):
            print("Your opponent has already placed an O in that position. Please try another position.")
        else:
            game.board[chosen_position] = 1
            valid = 1

    game.check_end_condition

    if(game.check_end_condition == 1):
        print(" YOU WON!")
    elif(game.check_end_condition == 2):
        print("YOU LOST!")
    elif(game.check_end_condition == 3):
        print("YOU TIED!")
    else:
        opponent.update_available_positions(game.board)     #update the available spaces
        opponent.take_turn(game.board)                      #Place an O
    
    game.display()                                #displays the board




game.display()