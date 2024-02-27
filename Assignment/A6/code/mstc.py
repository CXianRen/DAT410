import numpy as np
from collections import defaultdict

np.random.seed(42)

UCB_C = 1.4 #

class GStep(object):
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
      
class TTTGameState(object):
    x = 1
    o = -1

    def __init__(self, state, next_to_move=1):
        self.board = state
        self.board_size = state.shape[0]
        self.next_to_move = next_to_move

    def game_result(self):
        # check if game is over
        # Calculate the sum of each column
        rowsum = np.sum(self.board, 0)
        # Calculate the sum of each row
        colsum = np.sum(self.board, 1)
        # Calculate the sum of the diagonal from top-left to bottom-right
        diag_sum_tl = self.board.trace()
        # Calculate the sum of the diagonal from top-right to bottom-left
        diag_sum_tr = self.board[::-1].trace()

        # Check if any row, column, or diagonal sum equals the board size
        if any(rowsum == self.board_size) or any(colsum == self.board_size) \
           or diag_sum_tl == self.board_size or diag_sum_tr == self.board_size:
            return 1.0  # Indicates player wins -x wins
        # Check if any row, column, or diagonal sum equals negative board size
        elif any(rowsum == -self.board_size) or any(colsum == -self.board_size) \
          or diag_sum_tl == -self.board_size or diag_sum_tr == -self.board_size:
            return -1.0  # Indicates player loses O wins
        # If the board is full and no player wins
        elif np.all(self.board != 0):
            return 0.0  # Indicates a draw
        else:
            return None  # Game is not over yet

    def is_game_over(self):
        return self.game_result() != None

    def move(self, move):
        new_board = np.copy(self.board)
        new_board[move.x, move.y] = move.value
        next_to_move = TTTGameState.o if self.next_to_move == TTTGameState.x else TTTGameState.x
        return TTTGameState(new_board, next_to_move)

    def get_legal_actions(self):
        indices = np.where(self.board == 0)
        # Create a list of GStep objects for each empty cell
        moves = []
        for coords in list(zip(indices[0], indices[1])):
            move = GStep(coords[0], coords[1], self.next_to_move)
            moves.append(move)

        # Return the list of GStep objects
        return moves

class MCTSNode(object):
    def __init__(self, state: TTTGameState, parent=None):
        self.visits = 0.
        self._results = defaultdict(int)
        self.score = 0
        self.state = state
        self.parent = parent
        self.children = []
        self.untried_actions = self.state.get_legal_actions()

    def q(self):
        wins = self._results[self.parent.state.next_to_move]
        loses = self._results[-1 * self.parent.state.next_to_move]
        # if (wins - loses == self.score):
        #     print("wins lose score: ", wins, loses, self.score)
        # return wins - loses
        return self.score * self.parent.state.next_to_move
    

    # expand
    def get_unvisited_child(self):
        action = self.untried_actions.pop()
        next_state = self.state.move(action)
        child_node = MCTSNode(next_state, parent=self)
        self.children.append(child_node)
        return child_node

    def is_terminal_node(self):
        return self.state.is_game_over()

    def rollout(self):
        # each time move will generate a new state, so we don't have to copy the original state
        current_rollout_state = self.state
        while not current_rollout_state.is_game_over():
            possible_moves = current_rollout_state.get_legal_actions()
            action = self.rollout_policy(possible_moves)
            current_rollout_state = current_rollout_state.move(action)
        return current_rollout_state.game_result()

    def backpropagate(self, result):
        self.visits += 1.
        self._results[result] += 1.
        # print("result: ", result)
        self.score += result
        if self.parent:
            self.parent.backpropagate(result)

    def is_fully_expanded(self):
        return len(self.untried_actions) == 0

    def best_child(self, c_param=UCB_C):
        # UB = Q(s,a) + c * sqrt(ln(N(s)) / N(s,a))
        choices_weights = [
            (c.q() / (c.visits)) + \
            c_param * np.sqrt((2 * np.log(self.visits) / (c.visits)))
            for c in self.children
        ]
        # if len(choices_weights) == 0:
        #     return None
        return self.children[np.argmax(choices_weights)]

    def rollout_policy(self, possible_moves):
        # choice the first one
        return possible_moves[0]
        # random policy
        # return possible_moves[np.random.randint(len(possible_moves))]

def MCTS(node: MCTSNode,simulations_number = 1000):
    def traverse(current_node):
        while not current_node.is_terminal_node():
            if not current_node.is_fully_expanded():
                return current_node.get_unvisited_child()
            else:
                current_node = current_node.best_child()
        return current_node

    root = node
    for _ in range(0, simulations_number):
            v = traverse(root)
            reward = v.rollout()
            v.backpropagate(reward)
        # exploitation only
    return root.best_child(c_param=0.)


def print_board(board):
    for i in range(board.shape[0]):
        for j in range(board.shape[0]):
            if board[i, j] == 1:
                print("X ", end=" ")
            elif board[i, j] == -1:
                print("O ", end=" ")
            else:
                print("_ ", end=" ")
        print()
    print(flush=True)


###  game loop USER VS Computer ###

# game loop
board_size = 3
computer_fist = False
# computer_fist = True


state = np.zeros((board_size, board_size))
initial_board_state = TTTGameState(state=state, next_to_move=1)
c_state = initial_board_state
if computer_fist:
    root = MCTSNode(state=initial_board_state, parent=None)
    best_node = MCTS(root,10)
    c_state = best_node.state

print("The game starts!")
print_board(c_state.board)

while True:
    i, j = map(int, input("Enter your move (row and column): ").split())
    while c_state.board[i,j] != 0:
        print("Invalid move. Please try again.", flush=True)
        i, j = map(int, input("Enter your move (row and column): ").split())
    
    move1 = GStep(i, j, -1)
    c_state = c_state.move(move1)
    print("Your move:")
    print_board(c_state.board)

    if c_state.is_game_over():
        if c_state.game_result() == 1.0:
            print("You lose!")
        if c_state.game_result() == 0.0:
            print("Draw!")
        if c_state.game_result() == -1.0:
            print("You Win!")
        break

    new_state = TTTGameState(state=c_state.board, next_to_move=1)
    root = MCTSNode(state=new_state, parent=None)
    best_node = MCTS(root,100)
    c_state = best_node.state
    print("Computer's move:")
    print_board(c_state.board)

    if c_state.is_game_over():
        if c_state.game_result() == 1.0:
            print("You lose!")
        if c_state.game_result() == 0.0:
            print("Draw!")
        if c_state.game_result() == -1.0:
            print("You Win!")
        break
    else:
        continue