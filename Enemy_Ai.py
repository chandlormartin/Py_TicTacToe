import random

class Enemy:
    def take_turn(self, board):
        if(board[0] == 2 and board[1] == 0 and board[2] == 2):
            board[1] = 2
        elif(board[0] == 2 and board[1] == 2 and board[2] == 0):
            board[2] = 2
        elif(board[0] == 0 and board[1] == 2 and board[2] == 2):
            board[0] = 2

        elif(board[0] == 2 and board[4] == 0 and board[8] == 2):
            board[4] = 2
        elif(board[0] == 0 and board[4] == 2 and board[8] == 2):
            board[0] = 2
        elif(board[0] == 2 and board[4] == 2 and board[8] == 0):
            board[8] = 2

        elif(board[0] == 0 and board[3] == 2 and board[6] == 2):
            board[0] = 2
        elif(board[0] == 2 and board[3] == 0 and board[6] == 2):
            board[3] = 2
        elif(board[0] == 2 and board[3] == 2 and board[6] == 0):
            board[6] = 2

        elif(board[1] == 0 and board[4] == 2 and board[7] == 2):
            board[1] = 2
        elif(board[1] == 2 and board[4] == 0 and board[7] == 2):
            board[4] = 2
        elif(board[1] == 2 and board[4] == 2 and board[7] == 0):
            board[7] = 2

        elif(board[2] == 0 and board[5] == 2 and board[8] == 2):
            board[2] = 2
        elif(board[2] == 2 and board[5] == 0 and board[8] == 2):
            board[6] = 2
        elif(board[2] == 2 and board[5] == 2 and board[8] == 0):
            board[8] = 2

        elif(board[2] == 0 and board[4] == 2 and board[6] == 2):
            board[2] = 2
        elif(board[2] == 2 and board[4] == 0 and board[6] == 2):
            board[4] = 2
        elif(board[2] == 2 and board[4] == 2 and board[6] == 0):
            board[6] = 2

        elif(board[3] == 0 and board[4] == 2 and board[5] == 2):
            board[3] = 2
        elif(board[3] == 2 and board[4] == 0 and board[5] == 2):
            board[4] = 2
        elif(board[3] == 2 and board[4] == 2 and board[5] == 0):
            board[5] = 2

        elif(board[6] == 0 and board[7] == 2 and board[8] == 2):
            board[6] = 2
        elif(board[6] == 2 and board[7] == 0 and board[8] == 2):
            board[7] = 2
        elif(board[6] == 2 and board[7] == 2 and board[8] == 0):
            board[8] = 2
        else:
            check = 0                                           #set a check flag to make sure an unused position is filled
            while(check == 0):
                position = random.randint(0, len(board)-1)      #get random number from 0-8 until the number is an available position
                if(board[position] == 0):                       #places a circle in a random unused spot and sets check to 1 to leave loop
                    board[position] = 2
                    check           = 1