"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    return X if sum(row.count(X) for row in board) <= sum(row.count(O) for row in board) else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))
    
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid move")
    
    i, j = action
    result_board = [row[:] for row in board]
    result_board[i][j] = player(board)
    return result_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None or len(actions(board)) == 0:
        return True
    
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    result = winner(board)

    return 1 if result == X else -1 if result == O else 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    def evaluate(state, alpha, beta, is_maximizing):
        if terminal(state): return utility(state)
        
        if is_maximizing:
            value = -float('inf')
            for action in actions(state):
                value = max(value, evaluate(result(state, action), alpha, beta, False))
                alpha = max(alpha, value)
                if alpha >= beta: break
            return value
        else:
            value = float('inf')
            for action in actions(state):
                value = min(value, evaluate(result(state, action), alpha, beta, True))
                beta = min(beta, value)
                if alpha >= beta: break
            return value
    
    best_action = None
    alpha = float("-inf")
    beta = float("inf")
    turn = player(board)

    if turn == O:
        temp = float("inf")
        for action in actions(board):
            v = evaluate(result(board, action), alpha, beta, True)
            if v < temp:
                temp = v
                best_action = action
    elif turn == X:
        temp = float("-inf")
        for action in actions(board):
            v = evaluate(result(board, action), alpha, beta, False)
            if v > temp:
                temp = v
                best_action = action
    else:
        raise Exception("Invalid player")

    return best_action
        

# def min_value(state, alpha, beta):
#     if terminal(state):
#         return utility(state)
    
#     v = float("inf")

#     for action in actions(state):
#         v = min(v, max_value(result(state, action), alpha, beta))
#         beta = min(beta, v)
#         if alpha >= beta:
#             break
        
#     return v


# def max_value(state, alpha, beta):
#     if terminal(state):
#         return utility(state)
    
#     v = float("-inf")

#     for action in actions(state):
#         v = max(v, min_value(result(state, action), alpha, beta))
#         alpha = max(alpha, v)
#         if alpha >= beta:
#             break
        
#     return v