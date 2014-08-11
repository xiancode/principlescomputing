"""
Mini-max Tic-Tac-Toe Player
"""

import poc_ttt_gui
import poc_ttt_provided as provided
#from poc_ttt_provided import * 

# Set timeout, as mini-max can take a long time
import codeskulptor
codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

def mm_move(board, player):
    """
    Make a move on the board.
    
    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    if board.check_win() != None:
        return SCORES[board.check_win()],(-1,-1)
    empty_list = board.get_empty_squares()
    game = {}
    for item in empty_list:
        current = board.clone()
        current.move(item[0],item[1], player)
        if current.check_win() == player:
            return SCORES[player],item
        score_pos_tuple = mm_move(current, provided.switch_player(player))
        score = score_pos_tuple[0]
        game[score] = item
    if player == provided.PLAYERX:
        temp_keys 	= game.keys()
        temp_score 	= max(temp_keys)
        return temp_score,game[temp_score]
    elif player == provided.PLAYERO:
        temp_keys 	= game.keys()
        temp_score 	= min(temp_keys)
        return temp_score,game[temp_score]

def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

# provided.play_game(move_wrapper, 1, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)

#board=provided.TTTBoard(3,False,[[PLAYERO,PLAYERO,EMPTY],[EMPTY,PLAYERX,PLAYERX],[EMPTY,EMPTY,EMPTY]])
#print board
#print mm_move(board,provided.PLAYERX)
