# tic-tac-toe game
COMPUTER = 2
PLAYER = 1
EMPTY = 0


class TicTacToe():
  def __init__(self, size = 3):
    self.size = size
    self.board = [0 for _ in range(size*size)]
    self.palyer_1_label = 'X ' 
    self.palyer_2_label = 'O '
    self.empty_label = '— '
    self.label_map = {0: self.empty_label, 1: self.palyer_1_label, 2: self.palyer_2_label}

  def set_move(self, i, j, player):
    if self.board[i * self.size + j] == 0:
      self.board[i * self.size + j] = player
      return True
    else:
      return False

  def copy(self):
    new_game = TicTacToe(self.size)
    new_game.board = self.board.copy()
    return new_game

def is_winner(game, player):
  # Check for win condition with size greater than 3
  # check rows
  for i in range(game.size):
    for j in range(game.size-2):
      if all([game.board[i*game.size+j + k] == player for k in range(3)]):
        return True
  # check columns
  for i in range(game.size-2):
    for j in range(game.size):
      if all([game.board[(i+k)*game.size+j] == player for k in range(3)]):
        return True
  # check diagonals
  for i in range(game.size-2):
    for j in range(game.size-2):
      if all([game.board[(i+k)*game.size+j+k] == player for k in range(3)]):
        return True
  # check anti-diagonals
  for i in range(0,game.size-2):
    for j in range(2, game.size):
      if all([game.board[(i+k)*game.size+j-k] == player for k in range(3)]):
        return True
  return False

def is_terminal(game):
  if all([x != 0 for x in game.board]):
    return True
  return False

def print_board(game):
  for i in range(game.size):
    for j in range(game.size):
      print(game.label_map[game.board[i*game.size+j]], end = '')
    print(flush=True)

def game_loop( computer_policy, board_size = 3):
  game = TicTacToe(board_size)
  print("start, input 'i j' to select the place. from 0 to %d:"% (board_size-1), flush=True)
  print_board(game)

  while True:
    # get input from the user
    i, j = map(int, input("Enter your move (row and column): ").split())
    while game.board[i* game.size + j] != 0:
        print("Invalid move. Please try again.")
        i, j = map(int, input("Enter your move (row and column): ").split())

    game.set_move(i, j, 1)
    print("player 1 move:", flush=True)
    print_board(game)

    if is_winner(game, 1):
      print("player 1 win")
      break
    if is_terminal(game):
      print("draw")
      break
    
    # computer move
    best_move = computer_policy(game)
    game.set_move(best_move//game.size, best_move%game.size, 2)
    print("computer move:", flush=True)
    print_board(game)
    
    if is_winner(game, 2):
      print("computer win")
      break
    if is_terminal(game):
      print("draw")
      break
