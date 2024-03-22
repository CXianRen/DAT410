from chess import *

# test set_move
game = tictactoe()
game.set_move(0)
assert game.board[0] == 1, "fail set move 1"

game.set_move(1)
assert game.board[1] == 2, "fail set move 2"

game.set_move(2)
assert game.board[2] == 1, "fail set move 3"

game.set_move(3)
assert game.board[3] == 2, "fail set move 4"

game.set_move(4)
assert game.board[4] == 1, "fail set move 5"

game.set_move(5)
assert game.board[5] == 2, "fail set move 6"

game.set_move(6)
assert game.board[6] == 1, "fail set move 7"

game.set_move(7)
assert game.board[7] == 2, "fail set move 8"

game.set_move(8)
assert game.board[8] == 1, "fail set move 9"

# test get_illegal_moves
game = tictactoe()
game.set_move(0)
game.set_move(1)
game.set_move(2)
assert game.get_illegal_moves() == [0, 1, 2], "fail get illegal moves 1"

game.set_move(3)
game.set_move(4)
game.set_move(5)
assert game.get_illegal_moves() == [0, 1, 2, 3, 4, 5], "fail get illegal moves 2"

game.set_move(6)
game.set_move(7)
game.set_move(8)
assert game.get_illegal_moves() == [0, 1, 2, 3, 4, 5, 6, 7, 8], "fail get illegal moves 3"

# test winner
game = tictactoe()
game.board = [1, 1, 1,
              0, 0, 0,
              0, 0, 0]
assert game.winner() == 1, "fail winner 1"

game.board = [0, 0, 0,
              2, 2, 2,
              0, 0, 0]
assert game.winner() == 2, "fail winner 2"

game.board = [0, 0, 0,
              0, 0, 0,
              1, 1, 1]
assert game.winner() == 1, "fail winner 3"

game.board = [1, 0, 0,
              1, 0, 0,
              1, 0, 0]
assert game.winner() == 1, "fail winner 4"

game.board = [0, 1, 0,
              0, 1, 0,
              0, 1, 0]
assert game.winner() == 1, "fail winner 5"

game.board = [0, 0, 1,
              0, 0, 1,
              0, 0, 1]
assert game.winner() == 1, "fail winner 6"

game.board = [1, 0, 0,
              0, 1, 0,
              0, 0, 1]
assert game.winner() == 1, "fail winner 7"

game.board = [0, 0, 1,
              0, 1, 0,
              1, 0, 0]
assert game.winner() == 1, "fail winner 8"

game.board = [1, 0, 0,
              0, 1, 0,
              0, 0, 2]
assert game.winner() == 0, "fail winner 9"

# test isterminal
game = tictactoe()
game.board = [1, 1, 1,
              2, 2, 2,
              1, 1, 1]
assert game.isterminal() == True, "fail isterminal 1"

game.board = [1, 1, 1,
              2, 2, 2,
              1, 1, 0]
assert game.isterminal() == False, "fail isterminal 2"

game.board = [1, 1, 1,
              2, 2, 2,
              1, 1, 2]
assert game.isterminal() == True, "fail isterminal 3"

# test deepcopy
import copy
game = tictactoe()
game.set_move(0)
game.set_move(1)
game.set_move(2)
game_copy = copy.deepcopy(game)
game_copy.set_move(3)
assert game.board[3] == 0, "fail deepcopy 1"

game.set_move(4)
game_copy = copy.deepcopy(game)
game_copy.set_move(5)
assert game.board[5] == 0, "fail deepcopy 2"
