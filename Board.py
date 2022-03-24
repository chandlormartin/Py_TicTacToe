class Tictactoe:
    board       = [0] * 9       #create empty board containing 9 spaces
    condition   = 0    
    def display_row(self, a, b, c):
        if(a == 0 and b == 0 and c == 0):
            print("        |      |     ")
            print("        |      |     ")
            print("        |      |     ")
            print("        |      |     ")

        if(a == 0 and b == 0 and c == 1):
            print("        |      |     ")
            print("        |      | \ / ")
            print("        |      |  X  ")
            print("        |      | / \ ")

        if(a == 0 and b == 1 and c == 0): 
            print("        |      |     ")
            print("        | \ /  |     ")
            print("        |  X   |     ")
            print("        | / \  |     ")

        if(a == 0 and b == 1 and c == 1): 
            print("        |      |     ")
            print("        | \ /  | \ / ")
            print("        |  X   |  X  ")
            print("        | / \  | / \ ")

        if(a == 1 and b == 0 and c == 0): 
            print("        |      |     ")
            print("   \ /  |      |     ")
            print("    X   |      |     ")
            print("   / \  |      |     ")

        if(a == 1 and b == 0 and c == 1): 
            print("        |      |     ")
            print("   \ /  |      | \ / ")
            print("    X   |      |  X  ")
            print("   / \  |      | / \ ")

        if(a == 1 and b == 1 and c == 1): 
            print("        |      |     ")
            print("   \ /  | \ /  |     ")
            print("    X   |  X   |     ")
            print("   / \  | / \  |     ")

        if(a == 1 and b == 1 and c == 1): 
            print("        |      |     ")
            print("   \ /  | \ /  | \ / ")
            print("    X   |  X   |  X  ")
            print("   / \  | / \  | / \ ")

        if(a == 0 and b == 0 and c == 2):
            print("        |      |  __  ")
            print("        |      | |  | ")
            print("        |      | |  | ")
            print("        |      | |__| ")

        if(a == 0 and b == 2 and c == 0): 
            print("        |  __  |      ")
            print("        | |  | |      ")
            print("        | |  | |      ")
            print("        | |__| |      ")

        if(a == 0 and b == 2 and c == 2): 
            print("        |  __  |  __  ")
            print("        | |  | | |  | ")
            print("        | |  | | |  | ")
            print("        | |__| | |__| ")

        if(a == 2 and b == 0 and c == 0): 
            print("    __  |      |      ")
            print("   |  | |      |      ")
            print("   |  | |      |      ")
            print("   |__| |      |      ")

        if(a == 2 and b == 0 and c == 2): 
            print("    __  |      |  __  ")
            print("   |  | |      | |  | ")
            print("   |  | |      | |  | ")
            print("   |__| |      | |__| ")

        if(a == 2 and b == 2 and c == 0): 
            print("    __  |  __  |      ")
            print("   |  | | |  | |      ")
            print("   |  | | |  | |      ")
            print("   |__| | |__| |      ")

        if(a == 2 and b == 2 and c == 2): 
            print("    __  |  __  |  __  ")
            print("   |  | | |  | | |  | ")
            print("   |  | | |  | | |  | ")
            print("   |__| | |__| | |__| ")

        if(a == 1 and b == 0 and c == 2):
            print("        |      |  __  ")
            print("   \ /  |      | |  | ")
            print("    X   |      | |  | ")
            print("   / \  |      | |__| ")

        if(a == 0 and b == 1 and c == 2):
            print("        |      |  __  ")
            print("        | \ /  | |  | ")
            print("        |  X   | |  | ")
            print("        | / \  | |__| ")

        if(a == 1 and b == 1 and c == 2):
            print("        |      |  __  ")
            print("   \ /  | \ /  | |  | ")
            print("    X   |  X   | |  | ")
            print("   / \  | / \  | |__| ")

        if(a == 1 and b == 2 and c == 0): 
            print("        |  __  |      ")
            print("   \ /  | |  | |      ")
            print("    X   | |  | |      ")
            print("   / \  | |__| |      ")

        if(a == 0 and b == 2 and c == 1): 
            print("        |  __  |      ")
            print("        | |  | | \ /  ")
            print("        | |  | |  X   ")
            print("        | |__| | / \  ")
        
        if(a == 1 and b == 2 and c == 1): 
            print("        |  __  |      ")
            print("   \ /  | |  | | \ /  ")
            print("    X   | |  | |  X   ")
            print("   / \  | |__| | / \  ")

        if(a == 1 and b == 2 and c == 2): 
            print("        |  __  |  __  ")
            print("   \ /  | |  | | |  | ")
            print("    X   | |  | | |  | ")
            print("   / \  | |__| | |__| ")

        if(a == 2 and b == 1 and c == 0): 
            print("    __  |      |      ")
            print("   |  | | \ /  |      ")
            print("   |  | |  X   |      ")
            print("   |__| | / \  |      ")

        if(a == 2 and b == 0 and c == 1): 
            print("    __  |      |      ")
            print("   |  | |      | \ /  ")
            print("   |  | |      |  X   ")
            print("   |__| |      | / \  ")

        if(a == 2 and b == 1 and c == 1): 
            print("    __  |      |      ")
            print("   |  | | \ /  | \ /  ")
            print("   |  | |  X   |  X   ")
            print("   |__| | / \  | / \  ")

        if(a == 2 and b == 1 and c == 2): 
            print("    __  |      |  __  ")
            print("   |  | | \ /  | |  | ")
            print("   |  | |  X   | |  | ")
            print("   |__| | / \  | |__| ")

        if(a == 2 and b == 2 and c == 1): 
            print("    __  |  __  |      ")
            print("   |  | | |  | | \ /  ")
            print("   |  | | |  | |  X   ")
            print("   |__| | |__| | / \  ")

    def display_key(self):
        print("0 | 1 | 2 ")
        print("3 | 4 | 5 ")
        print("6 | 7 | 8 ")

    def display(self):                                                  #displays the current board
        self.display_row(self.board[0], self.board[1], self.board[2])
        print("________|______|_______")
        self.display_row(self.board[3], self.board[4], self.board[5])
        print("________|______|_______")
        self.display_row(self.board[6], self.board[7], self.board[8])


    def check_end_condition(self):                                                #set condition to 1 if player won, 2 if player lost, 3 if a tie, or else does nothing
        if(self.board[0] == 1 and self.board[1] == 1 and self.board[2] == 1):
            self.condition = 1
        if(self.board[3] == 1 and self.board[4] == 1 and self.board[5] == 1):
            self.condition = 1
        if(self.board[6] == 1 and self.board[7] == 1 and self.board[8] == 1):
            self.condition = 1
        if(self.board[0] == 1 and self.board[3] == 1 and self.board[6] == 1):
            self.condition = 1
        if(self.board[1] == 1 and self.board[4] == 1 and self.board[7] == 1):
            self.condition = 1
        if(self.board[2] == 1 and self.board[5] == 1 and self.board[8] == 1):
            self.condition = 1
        if(self.board[0] == 1 and self.board[4] == 1 and self.board[8] == 1):
            self.condition = 1
        if(self.board[2] == 1 and self.board[4] == 1 and self.board[6] == 1):
            self.condition = 1

        if(self.board[0] == 2 and self.board[1] == 2 and self.board[2] == 2):
            self.condition = 2
        if(self.board[3] == 2 and self.board[4] == 2 and self.board[5] == 2):
            self.condition = 2
        if(self.board[6] == 2 and self.board[7] == 2 and self.board[8] == 2):
            self.condition = 2
        if(self.board[0] == 2 and self.board[3] == 2 and self.board[6] == 2):
            self.condition = 2
        if(self.board[1] == 2 and self.board[4] == 2 and self.board[7] == 2):
            self.condition = 2
        if(self.board[2] == 2 and self.board[5] == 2 and self.board[8] == 2):
            self.condition = 2
        if(self.board[0] == 2 and self.board[4] == 2 and self.board[8] == 2):
            self.condition = 2
        if(self.board[2] == 2 and self.board[4] == 2 and self.board[6] == 2):
            self.condition = 2

        if 0 not in self.board:
            self.condition = 3
