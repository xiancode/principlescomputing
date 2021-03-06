"""
Student portion of Zombie Apocalypse mini-project
"""

import random
import poc_grid
import poc_queue
import poc_zombie_gui

#import user35_EPZOWWGoUeaEemm as test
#import user35_glBKmHxUdD_0 as test

# global constants
EMPTY = 0 
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = "obstacle"
HUMAN = "human"
ZOMBIE = "zombie"


class Zombie(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None, 
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)  
        else:
            self._human_list = []
        
    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        poc_grid.Grid.clear(self)
        self._human_list = []
        self._zombie_list = []
        
    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row,col))
                
    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)  
          
    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        # replace with an actual generator
        for dummy_zombie in self._zombie_list:
            yield dummy_zombie
        #return

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row,col))
        
    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)
    
    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        # replace with an actual generator
        for dummy_human in self._human_list:
            yield dummy_human
        #return
        
    def compute_distance_field(self, entity_type):
        """
        Function computes a 2D distance field
        Distance at member of entity_queue is zero
        Shortest paths avoid obstacles and use distance_type distances
        """
        height = self.get_grid_height()
        #print height
        width  = self.get_grid_width()
        #print width
        visited_grid = poc_grid.Grid(height,width)
        #distance_field = []
        boundary = poc_queue.Queue()
        distance_field = [[self._grid_width * self._grid_height for dummy_col in range(self._grid_width)] 
                       for dummy_row in range(self._grid_height)]
        if entity_type == "human":
            for dummy_item in self._human_list:
                boundary.enqueue(dummy_item)
        elif entity_type == "zombie":
            for dummy_item in self._zombie_list:
                boundary.enqueue(dummy_item)
        
        for dummy_cell in boundary:
        #cell = boundary.dequeue()
            visited_grid.set_full(dummy_cell[0],dummy_cell[1])
            distance_field[dummy_cell[0]][dummy_cell[1]] = 0
            
        while len(boundary) > 0:
            neighbors = []
            cell = boundary.dequeue()
            #print cell
            neighbors = poc_grid.Grid.four_neighbors(self,cell[0], cell[1])
            for neighbor in neighbors:
                if visited_grid.is_empty(neighbor[0],neighbor[1]) and self.is_empty(neighbor[0],neighbor[1]):
                    visited_grid.set_full(neighbor[0],neighbor[1])
                    if distance_field[neighbor[0]][neighbor[1]] > distance_field[cell[0]][cell[1]] + 1:
                        distance_field[neighbor[0]][neighbor[1]] = distance_field[cell[0]][cell[1]] + 1
                    boundary.enqueue(neighbor)
        return distance_field

    
    def move_humans(self, zombie_distance):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        idx = 0
        for cell in self._human_list:
            dist_list = []
            #distances.append(dummy_humman)
            distance = zombie_distance[cell[0]][cell[1]]
            neighbors = poc_grid.Grid.eight_neighbors(self,cell[0], cell[1])
            #neighbors.append(cell[0],cell[1])
            for neighbor in neighbors:
                dist_list.append(zombie_distance[neighbor[0]][neighbor[1]])
            max_dist = max(dist_list)
            if distance > max_dist:
                pass
            else:
                for neighbor in neighbors:
                    if zombie_distance[neighbor[0]][neighbor[1]] == max_dist:
                        self._human_list[idx] = ((neighbor[0],neighbor[1]))
            idx += 1
                
                    
                
    
    def move_zombies(self, human_distance):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        idx = 0
        for cell in self._zombie_list:
            dist_list = []
            #distances.append(dummy_humman)
            distance = human_distance[cell[0]][cell[1]]
            neighbors = poc_grid.Grid.four_neighbors(self,cell[0], cell[1])
            #neighbors.append(cell[0],cell[1])
            for neighbor in neighbors:
                dist_list.append(human_distance[neighbor[0]][neighbor[1]])
            min_dist = min(dist_list)
            if distance < min_dist:
                pass
            else:
                for neighbor in neighbors:
                    if human_distance[neighbor[0]][neighbor[1]] == min_dist:
                        self._zombie_list[idx] = ((neighbor[0],neighbor[1]))
            idx += 1

# Start up gui for simulation - You will need to write some code above
# before this will work without errors

# poc_zombie_gui.run_gui(Zombie(30, 40))

#test.phase1_test(Zombie)
#test.phase2_test(Zombie)
#test.Zombie_Appocalypse_test(Zombie)
#test.phase3_test(Zombie)
