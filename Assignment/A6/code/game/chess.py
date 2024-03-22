# 

class abstract_chess:
    def __init__(self):
        self.board
        self.current_player
        self.next_player
        
    def set_move(self, move):
        pass
    
    def get_illegal_moves(self):
        pass
    
    def winner(self):
        pass
    
    def isterminal(self):
        pass


class tictactoe(abstract_chess):
    # 1 for player 1, 2 for player 2
    player_1 = 1
    player_2 = 2
    def __init__(self):
        self.board = [0 for _ in range(9)]
        # player 1 starts the game
        self.next_player = self.player_1
        
    
    def get_illegal_moves(self):
        return [i for i in range(9) if self.board[i] != 0]
    
    def set_move(self, move):
        # move is an integer from 0 to 8
        # if next player is 1, set the move to 1
        # if next player is 2, set the move to 2
        # switch the next player after setting the move
        if self.next_player == self.player_1:
            self.board[move] = self.player_1
            self.next_player = self.player_2
        else: 
            self.board[move] = self.player_2
            self.next_player = self.player_1
    
    def winner(self):
        # Check for win condition with size greater than 3
        # check rows
        for i in range(3):
            if all([self.board[i*3+j] == self.player_1 for j in range(3)]):
                return self.player_1
            if all([self.board[i*3+j] == self.player_2 for j in range(3)]):
                return self.player_2
            
        # check columns
        for j in range(3):
            if all([self.board[i*3+j] == self.player_1 for i in range(3)]):
                return self.player_1
            if all([self.board[i*3+j] == self.player_2 for i in range(3)]):
                return self.player_2
        
        # check diagonals
        if all([self.board[i*3+i] == self.player_1 for i in range(3)]):
            return self.player_1
        if all([self.board[i*3+i] == self.player_2 for i in range(3)]):
            return self.player_2
        
        # check anti-diagonals  
        if all([self.board[i*3+2-i] == self.player_1 for i in range(3)]):
            return self.player_1
        if all([self.board[i*3+2-i] == self.player_2 for i in range(3)]):
            return self.player_2
        
        return 0
    
    def isterminal(self):
        if all([x != 0 for x in self.board]):
            return True
        return False
    
    def __str__(self):
        return str(self.board)
    