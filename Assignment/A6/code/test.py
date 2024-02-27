import random

class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.wins = 0
        self.visits = 0

    def is_fully_expanded(self):
        return len(self.children) == len(self.state)

    def select_child(self):
        return max(self.children, key=lambda c: c.wins / c.visits + (2 * (self.visits / c.visits) ** 0.5) if c.visits > 0 else float('inf'))

    def add_child(self, child_state):
        child = Node(child_state, self)
        self.children.append(child)
        return child

    def update(self, result):
        self.visits += 1
        self.wins += result

class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.current_player = 'X'

    def get_legal_moves(self):
        return [i for i, v in enumerate(self.board) if v == ' ']

    def make_move(self, move):
        self.board[move] = self.current_player
        if self.check_winner():
            return 1 if self.current_player == 'X' else -1
        elif ' ' not in self.board:
            return 0
        else:
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return None

    def check_winner(self):
        lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for line in lines:
            if self.board[line[0]] == self.board[line[1]] == self.board[line[2]] != ' ':
                return True
        return False

    def display_board(self):
        for i in range(0, 9, 3):
            print(' | '.join(self.board[i:i+3]))
            if i < 6:
                print('-' * 9)

class MCTSPlayer:
    def __init__(self, num_iterations=1000):
        self.num_iterations = num_iterations

    def get_move(self, state):
        return mcts_search(state, self.num_iterations).state

def mcts_search(root_state, num_iterations):
    root_node = Node(root_state)

    for _ in range(num_iterations):
        node = root_node
        state = root_state[:]

        # Selection phase
        while not TicTacToe().check_winner():
            if not node.is_fully_expanded():
                child_state = random.choice(state)
                node = node.add_child(child_state)
                break
            else:
                node = node.select_child()
                state = node.state

        # Expansion phase
        if not TicTacToe().check_winner():
            legal_moves = TicTacToe().get_legal_moves()
            random_move = random.choice(legal_moves)
            state.append(random_move)
            node = node.add_child(state)

        # Simulation phase
        while not TicTacToe().check_winner():
            legal_moves = TicTacToe().get_legal_moves()
            random_move = random.choice(legal_moves)
            state.append(random_move)

        # Backpropagation phase
        result = 1 if TicTacToe().check_winner() == 'X' else -1 if TicTacToe().check_winner() == 'O' else 0
        while node is not None:
            node.update(result)
            node = node.parent

    return max(root_node.children, key=lambda c: c.visits)

def human_player(state):
    while True:
        try:
            move = int(input("Enter your move (0-8): "))
            if move in state.get_legal_moves():
                return move
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Example usage
def main():
    game = TicTacToe()
    player1 = human_player
    player2 = MCTSPlayer()

    while True:
        game.display_board()

        # Human player's move
        move = player1(game)
        game.make_move(move)
        if game.check_winner():
            game.display_board()
            print("You win!")
            break
        elif ' ' not in game.board:
            game.display_board()
            print("It's a draw!")
            break

        # MCTS player's move
        move = player2.get_move(game.board)
        game.make_move(move)
        if game.check_winner():
            game.display_board()
            print("MCTS Player wins!")
            break

if __name__ == "__main__":
    main()
