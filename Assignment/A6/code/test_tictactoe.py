from tictactoe import *

# test set_move
game = TicTacToe()
game.set_move(0,0,  1)
print_board(game)
assert game.board[0] == 1, "fail set move 1"

game = TicTacToe(4)
game.set_move(0,0,  1)
print_board(game)
assert game.board[0] == 1, "fail set move 1"

game = TicTacToe()
game.board=[1,1,1, 
            2,2,0,
            0,0,0,
           ]
assert is_winner(game, 1) == True, "fail is winner 1" 

game = TicTacToe()
game.board=[0,0,0, 
            2,2,0,
            1,1,1,
           ]
assert is_winner(game, 1) == True, "fail is winner 2" 

game = TicTacToe()
game.board=[1,0,0, 
            1,2,0,
            1,2,0,
           ]
assert is_winner(game, 1) == True, "fail is winner 3" 

game = TicTacToe()
game.board=[1,0,0, 
            2,1,0,
            0,2,1,
           ]
assert is_winner(game, 1) == True, "fail is winner 4" 

game = TicTacToe()
game.board=[0,0,1, 
            2,1,0,
            1,2,0,
           ]
assert is_winner(game, 1) == True, "fail is winner 5" 


game = TicTacToe()
game.board=[1,1,1,0, 
            2,2,0,0,
            0,0,0,0,
            1,0,0,0,
           ]
assert is_winner(game, 1) == True, "fail is winner 6" 

game = TicTacToe()
game.board=[1,0,1,1, 
            1,2,0,0,
            1,0,0,0,
            0,0,0,0,
           ]
assert is_winner(game, 1) == True, "fail is winner 7" 

game = TicTacToe(4)
game.board=[2,0,1,1, 
            1,0,0,0,
            1,0,1,0,
            1,0,0,1,
           ]
assert is_winner(game, 1) == True, "fail is winner 8" 

game = TicTacToe(4)
game.board=[2,0,1,1, 
            0,1,0,0,
            1,0,1,0,
            1,0,0,1,
           ]
assert is_winner(game, 1) == True, "fail is winner 9" 

game = TicTacToe(4)
game.board=[1,0,1,1, 
            0,1,0,0,
            1,0,1,0,
            1,0,0,0,
           ]
assert is_winner(game, 1) == True, "fail is winner 10" 


game = TicTacToe(4)
game.board=[1,0,1,0, 
            0,0,1,0,
            1,1,2,0,
            1,0,0,0,
           ]
assert is_winner(game, 1) == True, "fail is winner 11" 

game = TicTacToe(4)
game.board=[1,0,1,1, 
            0,0,1,0,
            1,1,2,0,
            0,0,0,0,
           ]
assert is_winner(game, 1) == True, "fail is winner 12" 