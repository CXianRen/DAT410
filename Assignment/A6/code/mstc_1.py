# MCST algorithm

# reference: https://int8.io/monte-carlo-tree-search-beginners-guide/
from tictactoe import *
import math
import random   

UBC_C = 1.41 # recommended value for UBC_C is sqrt(2)

class Node():
    def __init__(self, game:TicTacToe, parent=None):
        self.game = game
        self.parent = parent
        self.child_count = sum([1 for x in game.board if x == EMPTY])
        self.player = COMPUTER if parent and parent.player == PLAYER else PLAYER

        self.children = [] # visited
        self.visits = 0
        self.score = 0
        self.is_expanded = False

    def copy(self):
        new_node = Node(self.game.copy())
        new_node.children = self.children.copy()
        new_node.visits = self.visits
        new_node.score = self.score
        new_node.is_expanded = self.is_expanded
        new_node.player = self.player
        return new_node

def rollout_policy(node: Node):
    # pick the first empty cell and play
    possible_moves = []
    for i in range(node.game.size):
        for j in range(node.game.size):
            if node.game.board[i * node.game.size + j] == EMPTY:
                possible_moves.append(i * node.game.size + j)

    if len(possible_moves) < 0:
        return node
    
    # position = random.choice(possible_moves)
    position=possible_moves[0]

    # print("select position:%d" % position)
    node.game.set_move(position//node.game.size, position%node.game.size, 3 - node.player)
    # update the player
    # print("update player: %d to %d" %(node.player, 3- node.player))
    node.player = 3 - node.player

    return node

def terminal(node: Node):
    if node is None:
        return True

    if is_winner(node.game, node.player) or \
        is_winner(node.game, 3 - node.player):
        return True
    if is_terminal(node.game):
        return True
    return False

def result(node: Node):
    if is_winner(node.game,COMPUTER):
        return 1
    if is_winner(node.game,PLAYER):
        return -1
    return 0

def rollout(node : Node, callback= None):
    # when similating the game, we don't save the simulated game.
    tnode = node.copy()
    while not terminal(tnode):
        tnode = rollout_policy(tnode)
        # for debug 
        if callback is not None:
            callback(tnode)
        # for debug
            
    # reutrn the score of the game
    return result(tnode)

def fully_expanded(node: Node):
    return node.child_count == len(node.children)

def best_ucb(node: Node, c = UBC_C):
    best_score = -math.inf
    best_node = None
    for child in node.children:
        if child.visits == 0:
            return child
        score = child.score if child.player == COMPUTER else -child.score  / child.visits + \
            c * math.sqrt(math.log(node.visits) / child.visits)
        if score > best_score:
            best_score = score
            best_node = child
    return best_node
       
def pick_unvisited(node: Node):
    # pick a unvisited children. not in childeren list
    for i in range(node.game.size):
        for j in range(node.game.size):
            if node.game.board[i * node.game.size + j] == EMPTY:
                new_game = node.game.copy()
                new_game.set_move(i, j, COMPUTER if node.player == PLAYER else PLAYER)
                
                # an un visited game
                is_unvisited = True 
                for child in node.children:
                    if child.game.board == new_game.board:
                        is_unvisited = False

                if is_unvisited == False:
                    continue
                         
                # print("un visted kid")
                new_node = Node(new_game, node)
                node.children.append(new_node)
                return new_node
    return node

def traverse(node: Node):
    while not terminal(node):
        if not fully_expanded(node):    
            return pick_unvisited(node)
        else:
            node = best_ucb(node)
    return node # in case no children are present / node is terminal

def backpropagate(node: Node, result):
    while node is not None:
        node.visits += 1
        node.score += result
        node = node.parent

def monte_carlo_tree_search_max_iteration(iterations, root: Node):
    while iterations:
        leaf = traverse(root) # leaf = unvisited node 
        if fully_expanded(leaf) is True:
            break
        simulation_result = rollout(leaf)
        backpropagate(leaf, simulation_result)
        iterations -=1
    return best_ucb(root, 0)


def mcts_plolicy(game: TicTacToe):
    root = Node(game)
    best_node = monte_carlo_tree_search_max_iteration(1000, root)
    for i in range(game.size * game.size):
        if game.board[i] != best_node.game.board[i]:
            return i


if __name__ == "__main__":
  game_loop(mcts_plolicy, board_size=3)