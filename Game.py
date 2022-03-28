import Board                                        #imports the file containing the game board
import Enemy_Ai                                     #imports the file containing the enemy AI

game            = Board.Tictactoe()                 #create instance of the board
opponent        = Enemy_Ai.Enemy()                  #create instance of opponent
turn_count      = 0                                 #counts how many turns the player has taken
while(game.condition == 0):
    valid = 0                                       #sets variable checking for input validity to 0

    print("Turn: ", turn_count)
    game.display()                                  #displays the board
    game.display_key()                              #displays the key for the game
    print("Please enter the number of the position you would like to place an X in.")

    while(valid == 0):
        temp = input()                              #takes in what position the player will place an X into

        if(temp < '0' or temp > '8'):
            print("Sorry, that isnt a valid position. Please try again.")
        else:
            chosen_position = int(temp)             #gets an integer version of temp

            if(chosen_position > len(game.board) or chosen_position < 0):
                print("Sorry, that position doesn't exist. Please try again.")
            elif(game.board[chosen_position] == 1):
                print("You have already placed an X in that position. Please try another position")
            elif(game.board[chosen_position] == 2):
                print("Your opponent has already placed an O in that position. Please try another position.")
            else:
                game.board[chosen_position] = 1     #sets the chosen position to 1
                valid = 1                           #sets valid to 1 to exit the loop

    game.check_end_condition()                      #checks if the player won or tied the game and changes game.condition if so            
    turn_count += 1                                 #increments the turn counter

    if(game.condition == 1):
        print(" \tYOU WON!")
    elif(game.condition == 3):
        print("\tYOU TIED!")
    else:
        opponent.take_turn(game.board)              #opponent takes their turn

    game.check_end_condition()                      #checks if the opponant won or tied the game and changes game.condition if so  
  
    if(game.condition == 2):
        print("\tYOU LOST!")
    if(game.condition == 3):
        print("\tYOU TIED!")

game.display()                                      #displays the final board