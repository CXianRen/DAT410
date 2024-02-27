from mstc_1 import *

# test rollout_policy
game = TicTacToe()
n = Node(game)
n = rollout_policy(n)
# print_board(n.game)
# print("----")
assert n.game.board[0]==2, "fail rollout_policy 1"

n = rollout_policy(n)
# print_board(n.game)
# print("----")
assert n.game.board[1]==1, "fail rollout_policy 2"

n = rollout_policy(n)
# print_board(n.game)
# print("----")
assert n.game.board[2]==2, "fail rollout_policy 3"

# test terminate
game = TicTacToe()
game.board=[1,2,1, 
            2,1,2,
            1,0,0,
           ]
n = Node(game)
assert terminal(n)==True, "fail terminal 1"
assert result(n) == -1, "fail result 1"

game.board=[1,2,1, 
            1,2,2,
            1,0,0,
           ]
n = Node(game)
assert terminal(n)==True, "fail terminal 2"
assert result(n) == -1, "fail result 2"

game.board=[1,1,1, 
            2,0,2,
            1,0,0,
           ]
n = Node(game)
assert terminal(n)==True, "fail terminal 3"
assert result(n) == -1, "fail result 3"

game.board=[1,0,2, 
            2,1,2,
            1,0,1,
           ]
n = Node(game)
assert terminal(n)==True, "fail terminal 4"
assert result(n) == -1, "fail result 4"

game.board=[2,0,1, 
            2,1,2,
            1,0,1,
           ]
n = Node(game)
assert terminal(n)==True, "fail terminal 5"
assert result(n) == -1, "fail result 5"

game.board=[2,0,1, 
            2,1,2,
            2,0,1,
           ]
n = Node(game)
assert terminal(n)==True, "fail terminal 6"
assert result(n) == 1, "fail result 5"


# test rollout
def print_rollout_middle_stage(n: Node):
  print("--------")
  print_board(n.game)
  pass

game = TicTacToe()
n = Node(game)

print("test rollout 1")
assert rollout(n, print_rollout_middle_stage) == 1, "fail rollout 1"

game = TicTacToe()
game.board=[1,0,0, 0,0,0, 0,0,0]
n = Node(game)

print("test rollout 2")
assert rollout(n, print_rollout_middle_stage) == -1, "fail rollout 2"

game = TicTacToe()
game.board=[1,0,0, 0,2,0, 0,0,1]
n = Node(game)

print("test rollout 3")
assert rollout(n, print_rollout_middle_stage) == -1, "fail rollout 3"


game = TicTacToe()
game.board=[1,2,1, 0,2,2, 2,1,1]
n = Node(game)
n.player=COMPUTER
print("PLAYER:",n.player)

print("test rollout 4")
assert rollout(n, print_rollout_middle_stage) == 0, "fail rollout 4"


# test fully_expanded
game = TicTacToe()
n = Node(game)
assert fully_expanded(n) == False, "fail fully_expanded 1"

game = TicTacToe()
n = Node(game)
for i in range(n.game.size):
  for j in range(n.game.size):
    if n.game.board[i*n.game.size+j] == EMPTY:
      # save one to children
      new_game = n.game.copy()
      new_game.set_move(i, j, COMPUTER if n.player == PLAYER else PLAYER)
      new_node = Node(new_game, n)
      n.children.append(new_node)
      break
  break
assert len(n.children) == 1, "fail add children 1"
assert fully_expanded(n) == False, "fail fully_expanded 2"

game = TicTacToe()
n = Node(game)
for i in range(n.game.size):
  for j in range(n.game.size):
    if n.game.board[i*n.game.size+j] == EMPTY:
      # save one to children
      new_game = n.game.copy()
      new_game.set_move(i, j, COMPUTER if n.player == PLAYER else PLAYER)
      new_node = Node(new_game, n)
      n.children.append(new_node)
      break
assert len(n.children) == 3, "fail add children 2"
assert fully_expanded(n) == False, "fail fully_expanded 3"



game = TicTacToe()
n = Node(game)
for i in range(n.game.size):
  for j in range(n.game.size):
    if n.game.board[i*n.game.size+j]  == EMPTY:
      # save one to children
      new_game = n.game.copy()
      new_game.set_move(i, j, COMPUTER if n.player == PLAYER else PLAYER)
      new_node = Node(new_game, n)
      n.children.append(new_node)

assert len(n.children) == 9, "fail add children 3"
assert fully_expanded(n) == True, "fail fully_expanded 4"

# test pick_unvisited
game = TicTacToe()
n = Node(game)

unvisted_n = pick_unvisited(n)
assert n.player != unvisted_n.player, "fail pick_unvisited 1 player"
assert n.children[0].game.board == unvisted_n.game.board, "fail pick_unvisited 1 board"
assert n.children[0].game.board[0] == 2, "fail pick_unvisited 1 value"

unvisted_n = pick_unvisited(n)
assert n.player != unvisted_n.player, "fail pick_unvisited 2 player"
assert n.children[1].game.board == unvisted_n.game.board, "fail pick_unvisited 2 board"
assert n.children[1].game.board[1] == 2, "fail pick_unvisited 2 value"
assert n.children[1].game.board[0] == 0, "fail pick_unvisited 2 value"