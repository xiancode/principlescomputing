"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided
#import user34_Uc9ea2tRiN_0 as test_ttt
#import user35_PIk21NjpAa_0 as tests
#import user35_UuNOhyrtdu_2 as tests

# Constants for Monte Carlo simulator
# Change as desired
NTRIALS = 10    # Number of trials to run
MCMATCH = 1.0  # Score for squares played by the machine player
MCOTHER = 1.0  # Score for squares played by the other player
    
# Add your functions here.

def mc_trial(board,player):
    """
    play the game,change the player
    """
    while board.check_win() is None:
        gamelist = board.get_empty_squares()
        [row,col] = random.choice(gamelist)
        board.move(row,col,player)
        player = provided.switch_player(player)
        
def mc_update_scores(scores,board,player):
    """
    update scores rely on board
    """
    current_board = board.clone()
    dim = board.get_dim()

    if board.check_win() == provided.DRAW or board.check_win() == None:
        return
    player1 = current_board.check_win()
    for row in range(dim):
        for col in range(dim):
            if current_board.square(row,col) == player1:
                scores[row][col] += MCMATCH
            elif current_board.square(row,col) == provided.EMPTY:
                scores[row][col] += 0 
            else:
                scores[row][col] -= MCOTHER
                
def get_best_move(board, scores):
    """
    get best move
    """
    current = board.clone()
    gamelist = current.get_empty_squares()
    if len(gamelist) == 0:
        return 
    dim = current.get_dim()
    best_score = float("-inf")
    tmp = []
    scores_list = []
    return_list = []
    
    for [row,col] in gamelist:
        tmp.append(scores[row][col])
    best_score = max(tmp)

    for row in range(dim):
        for col in range(dim):
            if scores[row][col] == best_score:
                scores_list.append((row,col))
                 
    for scr_index in scores_list:
        for bor_index in gamelist:
            if scr_index == bor_index:
                return_list.append(scr_index)
    return random.choice(return_list)


def mc_move(board, player, trials):
    """
    move
    """

    dim = board.get_dim()
    
    scores = [[0 for dummy_row in range(dim)] for dummy_col in range(dim)]
    for dummy in range(trials):
        current = board.clone()
        mc_trial(current,player)
        mc_update_scores(scores,current,player)
    
    best_move = get_best_move(board, scores)
    return best_move
    
    
    
     
        
#test_ttt.test_trial(mc_trial)
#print
#test_ttt.test_update_scores(mc_update_scores, MCMATCH, MCOTHER)
# print
#test_ttt.test_best_move(get_best_move)


# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

# provided.play_game(mc_move, NTRIALS, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
#tests.test_mc_trial(mc_trial)                                             # tests for mc_trial

#tests.test_mc_update_scores(mc_update_scores, MCMATCH, MCOTHER)           # tests for mc_update_scores

#tests.test_get_best_move(get_best_move)                                   # tests for get_best_move

#tests.test_mc_move(mc_move, NTRIALS)
