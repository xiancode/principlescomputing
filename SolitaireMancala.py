"""
Student facing implement of solitaire version of Mancala - Tchoukaillon

Goal: Move as many seeds from given houses into the store
"""
import poc_mancala_testsuite
#import poc_mancala_gui
#import copy

class SolitaireMancala:
    """
    Simple class that implements Solitaire Mancala
    """
    configuration = []
    
    def __init__(self):
        """
        Create Mancala game with empty store and no houses
        """
        self.configuration = [0]
    
    def set_board(self, configuration):
        """
        Take the list configuration of initial number of seeds for given houses
        house zero corresponds to the store and is on right
        houses are number in ascending order from right to left
        """
        self.configuration = []
        #print len(configuration)
        for i in range(len(configuration)):
            self.configuration.append(configuration[i])
        #self.configuration = copy.deepcopy(configuration)
    
    def __str__(self):
        """
        Return string representation for Mancala board
        """
        #res_str = ""
        #for conf in self.configuration:
        #    res_str += str(conf) + ','
        #return res_str
        result = []
        for conf in self.configuration:
            result.append(conf)
        #result = copy.deepcopy(self.configuration)
        result.reverse()
        res_str = str(result)
        return res_str
    
    def get_num_seeds(self, house_num):
        """
        Return the number of seeds in given house on board
        """
        return self.configuration[house_num]

    def is_game_won(self):
        """
        Check to see if all houses but house zero are empty
        """
        
        for  i  in range(1,len(self.configuration)):
            if self.configuration[i] != 0:
                return False
        return True

    
    def is_legal_move(self, house_num):
        """
        Check whether a given move is legal
        """
        if house_num == 0:
            return False
        if self.configuration[house_num] == house_num:
            return True
        else:
            return False

    
    def apply_move(self, house_num):
        """
        Move all of the stones from house to lower/left houses
        Last seed must be played in the store (house zero)
        """
        if self.is_legal_move(house_num):
            for i in range(0,house_num):
                self.configuration[i] += 1
            self.configuration[house_num] = 0

    def choose_move(self):
        """
        Return the house for the next shortest legal move
        Shortest means legal move from house closest to store
        Note that using a longer legal move would make smaller illegal
        If no legal move, return house zero
        """
        con_size = len(self.configuration)
        for i in range(1,con_size):
            if self.is_legal_move(i):
                return i
        return 0
    
    def plan_moves(self):
        """
        Return sequence of shortest legal moves until none are available
        Not used in GUI version, only for machine testing
        """
        movelist = []
        cur_pos = self.choose_move()
        while(cur_pos != 0):
            movelist.append(cur_pos)
            self.apply_move(cur_pos)
            cur_pos = self.choose_move()
        return movelist
        
        #print self.is_game_won()
        #print self.configuration
        


poc_mancala_testsuite.run_test(SolitaireMancala)
#poc_mancala_gui.run_gui(SolitaireMancala())
