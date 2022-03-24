import random

class Enemy:
    available_positions = [0, 1, 2, 3, 4, 5, 6, 7, 8]   #A list of all available board positions

    def update_available_positions(self, board):
        for i in self.available_positions:              #iterates through board, updating the list of unused spaces
            if(board[self.available_positions[i]] != 0):
                del self.available_positions[i]


    def take_turn(self, board):
        board[random.randint(0, self.available_positions.__len__)] = 2  #places a cirlce in a random unused spot