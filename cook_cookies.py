"""
Cookie Clicker Simulator
"""
#import user34_1yyodNweJj_0 as init_test
#import user34_gwOBYcB0vg_5 as wait_test
#import user34_JegqHUeyeq_1 as time_until_test
#import user34_CX25TCXsrD_4 as buy_test
#import user34_muNP84fR8e_2 as testsuite
#import user34_GhjnBEJSmI_10 as test_suite
import simpleplot

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

import poc_clicker_provided as provided
import math
# Constants
SIM_TIME = 10000000000.0

class ClickerState:
    """
    Simple class to keep track of the game state.
    """
    
    def __init__(self):
        self._currentcookies = 0.0
        self._totalcookies = 0.0
        self._totalcookies = 0.0
        self._currenttime = 0.0 
        self._currentcps = 1.0
        self._item = None
        self._history = [(0.0,None,0.0,0.0)]
        
        
    def __str__(self):
        """
        Return human readable state
        """
        return ""
        
    def get_cookies(self):
        """
        Return current number of cookies 
        (not total number of cookies)
        
        Should return a float
        """
        return self._currentcookies
    
    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._currentcps
    
    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self._currenttime
    
    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: (0.0, None, 0.0, 0.0)
        """
        return self._history

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        if self._currentcookies >= cookies or cookies == 0:
            return 0.0
        else:
            return math.ceil((cookies - self._currentcookies)/self._currentcps)
        
    
    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0
        """
        if time < 0:
            pass
        else:
            self._currenttime += time
            self._currentcookies += time * self._currentcps
            self._totalcookies += time * self._currentcps
            
    
    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if self._currentcookies < cost:
            pass
        else:
            self._history.append((self._currenttime,item_name,cost,self._totalcookies))
            self._currentcookies -= cost
            #self._totalcookies -= cost
            self._item = item_name
            self._currentcps += additional_cps
   
    
def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to game.
    """

    # Replace with your code
    #print duration
    click = ClickerState()
    build_clone=build_info.clone()
    #print click.get_time()
    while click.get_time() <= duration:
        item = strategy(click.get_cookies(),click.get_cps(),duration-click.get_time(),build_clone)
        #print 'buy',item
        #print '--------------------------'
        if item == None: 
            click.wait(duration-click.get_time())
            break
        else:
            #print 'item',item
            cost = build_clone.get_cost(item)
            #print 'cost',cost
            #print 'cps',build_clone.get_cps(item)
            #print 'history',click.get_history()
            if click.get_cookies() >= cost:
                click.buy_item(item,cost,build_clone.get_cps(item))
                build_clone.update_item(item)
                #print 'x'
            else:
                elapsed_time = click.time_until(cost)
                #print 'elapsed_time:',elapsed_time
                #print 'duration : ',duration
                #print 'get_time():',click.get_time()
                if elapsed_time > duration - click.get_time():
                    #print 'time',duration - click.get_time()
                    click.wait(duration-click.get_time())
                    #print click.get_cookies()
                    #print 'Y'
                    #print click.get_cookies()
                    #print click._totalcookies
                    break
                else:
                    click.wait(elapsed_time)
                    #print 'cookies',click.get_cookies()
                    #print 'cps',click.get_cps()
                    click.buy_item(item,cost,build_clone.get_cps(item))
                    #print 'Cursor cost',build_clone.get_cost("Cursor")
                    #print 'Cursor cps',build_clone.get_cps("Cursor")
                    #print click.get_cookies()
                    #print click.get_cps()
                    #print '---------------------------'
                    build_clone.update_item(item)
    return click
    #return ClickerState()


def strategy_cursor(cookies, cps, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic strategy does not properly check whether
    it can actually buy a Cursor in the time left.  Your strategy
    functions must do this and return None rather than an item you
    can't buy in the time left.
    """
    return "Cursor"

def strategy_none(cookies, cps, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that you can use to help debug
    your simulate_clicker function.
    """
    return None

def strategy_cheap(cookies, cps, time_left, build_info):
    """
    """
    build_clone = build_info.clone()
    items = build_clone.build_items()
    cheap_value = float("inf")
    cheap_item = None
    for item in items:
        value = build_clone.get_cost(item)
        if cheap_value > value:
            cheap_value = value
            cheap_item = item
    if cheap_value > cps * time_left + cookies:
        return None
    else:
        return cheap_item

def strategy_expensive(cookies, cps, time_left, build_info):
    """
    """
    build_clone = build_info.clone()
    items = build_clone.build_items()
    #expensive_value = float("-inf")
    #expensive_item = None
    dic = {}
    value_list = []
    for item in items:
        value = build_clone.get_cost(item)
        if value <= cookies + cps * time_left:
            dic[value] = item
            value_list.append(value)
    if not dic:
        return None
    else:
        value_list.sort()
        key = value_list[-1]
        return dic[key]
    


def strategy_best(cookies, cps, time_left, build_info):
    """
    """
    return None
        
def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation with one strategy
    """
    #BuildInfo({'Cursor': [15.0, 50.0]}, 1.15),
    #state = simulate_clicker(provided.BuildInfo(), time, strategy)
    
    state = simulate_clicker(provided.BuildInfo({'Cursor': [15.0, 50.0]}, 1.15), 16, strategy_cursor)
    print strategy_name, ":", state
    #print state.get_time()
    #print state.get_cookies()
    #print state.get_cps()
    #print state._totalcookies
    #state2 = simulate_clicker(provided.BuildInfo(), 15.0, strategy_cursor)
    #print state2

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    # history = state.get_history()
    # history = [(item[0], item[3]) for item in history]
    # simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)

def run():
    """
    Run the simulator.
    """    
    run_strategy("Cursor", SIM_TIME, strategy_cursor)
    #run_strategy("Cursor", 16, strategy_cursor)

    # Add calls to run_strategy to run additional strategies
    # run_strategy("Cheap", SIM_TIME, strategy_cheap)
    # run_strategy("Expensive", SIM_TIME, strategy_expensive)
    # run_strategy("Best", SIM_TIME, strategy_best)
    
run()
#print strategy_expensive(0.0, 1.0, 5.0, provided.BuildInfo({'A': [5.0, 1.0], 'C': [50000.0, 3.0], 'B': [500.0, 2.0]}, 1.15))
#init_test.run_test(ClickerState)
#wait_test.run_test(ClickerState)
#time_until_test.run_test(ClickerState)
#buy_test.run_test(ClickerState)
#testsuite.run_tests(ClickerState,simulate_clicker,strategy_cursor)
#test_suite.run_simulate_clicker_tests(simulate_clicker,strategy_none,strategy_cursor)
#test_suite.run_clicker_state_tests(ClickerState)
    

