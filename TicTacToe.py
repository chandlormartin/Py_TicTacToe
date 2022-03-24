class Tictactoe:
    board = [0] * 9       #create empty board containing 9 spaces
    
    def display_row(self, a, b, c):
        if(a == 0 and b == 0 and c ==0):
            print("        |      |     ")
            print("        |      |     ")
            print("        |      |     ")
            print("        |      |     ")

        if(a == 0 and b == 0 and c ==1):
            print("        |      |     ")
            print("        |      | \ / ")
            print("        |      |  X  ")
            print("        |      | / \ ")

        if(a == 0 and b == 1 and c ==0): 
            print("        |      |     ")
            print("        | \ /  |     ")
            print("        |  X   |     ")
            print("        | / \  |     ")

        if(a == 0 and b == 1 and c ==1): 
            print("        |      |     ")
            print("        | \ /  | \ / ")
            print("        |  X   |  X  ")
            print("        | / \  | / \ ")

        if(a == 1 and b == 0 and c ==0): 
            print("        |      |     ")
            print("   \ /  |      |     ")
            print("    X   |      |     ")
            print("   / \  |      |     ")

        if(a == 1 and b == 0 and c ==1): 
            print("        |      |     ")
            print("   \ /  |      | \ / ")
            print("    X   |      |  X  ")
            print("   / \  |      | / \ ")

        if(a == 1 and b == 1 and c ==1): 
            print("        |      |     ")
            print("   \ /  | \ /  |     ")
            print("    X   |  X   |     ")
            print("   / \  | / \  |     ")

        if(a == 1 and b == 1 and c ==1): 
            print("        |      |     ")
            print("   \ /  | \ /  | \ / ")
            print("    X   |  X   |  X  ")
            print("   / \  | / \  | / \ ")

        if(a == 1 and b == 0 and c ==1): 
            print("        |      |     ")
            print("   \ /  |      | \ / ")
            print("    X   |      |  X  ")
            print("   / \  |      | / \ ")

        if(a == 0 and b == 0 and c ==0):
            print("        |  __  |     ")
            print("   \ /  | |  | |     ")
            print("    X   | |  | |     ")
            print("   / \  | |__| |     ")
    
    def display(self):
        self.display_row(self.board[0], self.board[1], self.board[2])
        print("_______|______|_______")
        self.display_row(self.board[3], self.board[4], self.board[5])
        print("______________________")
        self.display_row(self.board[6], self.board[7], self.board[8])

game = Tictactoe()

game.display()
