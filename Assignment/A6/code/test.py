import math

# 定义井字棋的大小
BOARD_SIZE = 3
# 定义玩家
EMPTY = 0
PLAYER_X = 1
PLAYER_O = 2

# 检查是否有一方获胜
def is_winner(board, player):
    # 检查行和列
    for i in range(BOARD_SIZE):
        if all(board[i][j] == player for j in range(BOARD_SIZE)) or \
           all(board[j][i] == player for j in range(BOARD_SIZE)):
            return True
    # 检查对角线
    if all(board[i][i] == player for i in range(BOARD_SIZE)) or \
       all(board[i][BOARD_SIZE - i - 1] == player for i in range(BOARD_SIZE)):
        return True
    return False

# 检查游戏是否结束（平局）
def is_draw(board):
    return all(board[i][j] != EMPTY for i in range(BOARD_SIZE) for j in range(BOARD_SIZE))

# 打印游戏棋盘
def print_board(board):
    for row in board:
        print(" ".join(["X" if cell == PLAYER_X else "O" if cell == PLAYER_O else "-" for cell in row]))
    print()

# Minimax算法
def minimax(board, depth, maximizing_player):
    # 判断当前游戏状态
    if is_winner(board, PLAYER_X):
        return 1
    elif is_winner(board, PLAYER_O):
        return -1
    elif is_draw(board) or depth == 0:
        return 0

    # 初始化最大值和最小值
    if maximizing_player:
        max_eval = -math.inf
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    eval = minimax(board, depth - 1, False)
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    eval = minimax(board, depth - 1, True)
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
        return min_eval

# 让电脑玩家选择最优动作
def computer_move(board):
    best_move = None
    best_eval = -math.inf
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_X
                eval = minimax(board, 9, False)
                board[i][j] = EMPTY
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

# 主程序
def main():
    # 初始化游戏棋盘
    board = [[EMPTY] * BOARD_SIZE for _ in range(BOARD_SIZE)]

    # 游戏循环
    while True:
        # 电脑玩家选择动作
        print("Computer's move:")
        computer_move_row, computer_move_col = computer_move(board)
        board[computer_move_row][computer_move_col] = PLAYER_X
        print_board(board)

        # 检查是否有一方获胜
        if is_winner(board, PLAYER_X):
            print("Computer wins!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

        # 玩家选择动作
        player_move_row, player_move_col = map(int, input("Enter your move (row and column): ").split())
        while board[player_move_row][player_move_col] != EMPTY:
            print("Invalid move. Please try again.")
            player_move_row, player_move_col = map(int, input("Enter your move (row and column): ").split())
        board[player_move_row][player_move_col] = PLAYER_O
        print_board(board)

        # 检查是否有一方获胜
        if is_winner(board, PLAYER_O):
            print("Player wins!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
