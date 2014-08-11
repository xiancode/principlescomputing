"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
#import user35_oGFuhcPNLh_0 as score_testsuite
#import user35_uLOFnLQSJV29rFh_5 as expected_value_testsuite
#import user35_IM4UytH4mK_22 as tests
import codeskulptor
codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    if len(hand) == 0:
        return 0
    sums = []
    value = 0
    #print hand 
    for dummy_dice in hand:
        value = hand.count(dummy_dice)*dummy_dice
        sums.append(value)
    return max(sums)
    #return 0


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value of the held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    #print "held_dice",held_dice
    #print "num_die_sides",num_die_sides
    #print "num_free_dice",num_free_dice
    ans = 0.0
    tmp = [dummy for dummy in range(1,num_die_sides+1)]
    all_rolls = gen_all_sequences(tmp, num_free_dice)
    #print "all_rolls length ",len(all_rolls)
    
    
    score_list = []
    #expection = float("-inf")
    for dummy_roll in all_rolls:
        roll = held_dice + dummy_roll
        #print roll
        #if expection < score(roll):
            #expection = score(roll)
        score_list.append(score(roll))
    #print sum(score_list)
    #print len(score_list)
    ans = float(sum(score_list))/float(len(score_list))    
    return ans


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    ans = set([()])
    if len(hand) == 0:
        return ans
    
    masks = gen_all_sequences([0,1], len(hand))
    for mask in masks:
        idx = 0
        new_seq = list()
        for dummy_item in mask:
            if dummy_item != 0:
                new_seq.append(hand[idx])
                idx += 1
            else:
                idx += 1
        ans.add(tuple(new_seq))
                
                
    return ans
    #return set([()])



def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    bestvalue = 0.0
    bestroll = tuple()
    rolls = gen_all_holds(hand)
    #print "hand",hand
    #print "rolls length",len(rolls)
    for roll in rolls:
        value = expected_value(roll, num_die_sides, len(hand) - len(roll))
        if value > bestvalue:
            bestvalue = value
            bestroll = tuple(roll)
    return (bestvalue,bestroll)        
    #return (0.0, ())


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    
    
#run_example()

#score_testsuite.run_suite(score)
#expected_value_testsuite.run_suite(expected_value)
#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)

#tests.run_score_suite(score)
#tests.run_expected_value_suite(expected_value)
#tests.run_gen_all_holds_suite(gen_all_holds)
#tests.run_strategy_suite(strategy)     

                                       
    
    
    



