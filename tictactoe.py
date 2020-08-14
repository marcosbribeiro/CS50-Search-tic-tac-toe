"""
Tic Tac Toe Player

###############################

Marcos Ribeiro
#GITHub user: marcosbribeiro

# 05/15/20

###############################


"""

import math
import copy
import numpy as np

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
    count_X = 0
    count_O = 0
    if board == [[None, None, None],[None, None, None],[None, None, None]]:
        return X
    else:
        count_X = board[0].count("X") + board[1].count("X") + board[2].count("X")        
        count_O = board[0].count("O") + board[1].count("O") + board[2].count("O")
        
        if count_X > count_O:
            return O
        else:
            return X
            

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    next_actions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                next_actions.add((i,j))
    return next_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    result_board = copy.deepcopy(board)
    if board[action[0]][action[1]] != None:
      raise Exception('Not a valid action')
    else:
        result_board[action[0]][action[1]] = O if player(board) == O else X
        return result_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #Verify Rows
    for i in range(3):
        x = board[i].count("X")
        o = board[i].count("O")
        if x == 3:
            return "X"
        elif o == 3:
            return "O"
    else:
        board_transpose = np.array(board)
        board_transpose = board_transpose.T.tolist()
        for i in range(3):
            x = board_transpose[i].count("X")
            o = board_transpose[i].count("O")
            if x == 3:
                return X
            elif o == 3:
                return O
        else:
            a = board[0][0]
            b = board[1][1]
            c = board[2][2]
            d = board[2][0]
            e = board[0][2]
            if a == b and b == c:
                return a
            elif b == d and d == e:
                return b 
            
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) or not actions(board):
      return True
    else:
      return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """     
    if winner(board) == 'X':
      return 1
    elif winner(board) == 'O':
      return -1
    else:
      return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    global actions_explored
    actions_explored = 0

    def max_player(board):
      """ function to maximise score for 'X' player.

      """

      global actions_explored

      # If the game is over, return board value
      if terminal(board):
        return (utility(board), None)

      v = -math.inf
      best_action = None

      for action in actions(board):

        actions_explored += 1
        min_player_result = min_player(result(board, action))
        if min_player_result[0] > v:
          best_action = action
          v = min_player_result[0]
          
          if actions_explored > 20000:     # Limiting to much interations
              return (v, best_action)           

      return (v, best_action)


    def min_player(board): 
      """ function to minimise score for 'O' player.

      """
      global actions_explored

      if terminal(board):
        return (utility(board), None)

      v = math.inf
      best_action = None

      for action in actions(board):

        actions_explored += 1
        max_player_result = max_player(result(board, action))
        if max_player_result[0] < v:
          best_action = action
          v = max_player_result[0]
          
          #if actions_explored > 2000000:     # Limiting to much interations
          #    return (v, best_action)          

      return (v, best_action)


    # If the board is terminal, return None:
    if terminal(board):
      return None

    if player(board) == 'X':
      print('AI is exploring possible actions...')
      best_move = max_player(board)[1]
      print('Actions explored: ', actions_explored)
      return best_move
    else:
      print('AI is exploring possible actions...')
      best_move = min_player(board)[1]
      print('Actions explored: ', actions_explored)
      return best_move
 


    


