import Board        #imports my file containing the game board
import Enemy_Ai     #imports the enemy AI


game            = Board.Tictactoe() #create instance of the board
end_condition   = 0                 #set a default end condition to make players take turns until one of them wins

while(end_condition == 0):
    print("Please enter the number of the position you would like to place an X in.")
    




game.display()