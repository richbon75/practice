"""Imagine a robot sitting on the upper left corner of grid with
r rows and c columns. The robot can only move in two directions,
right and down, but certain cells are "off limits" such that the
robot cannot step on them. Design an algorithm to find a path for
the robot from the top left to the bottom right."""

from collections import deque
from copy import copy
from random import randint

class Grid(object):
    """A basic Grid class to make dealing with the grid easier."""

    def __init__(self, rows, columns):
        """Initialize the grid. Ever cell starts as '.' which
        means it it ok for the robot to walk on."""
        self.rows = rows
        self.columns = columns
        self.grid = list()
        self.exit = (rows-1, columns-1)
        for r in range(rows):
            row = list()
            for c in range(columns):
                row.append('.')
            self.grid.append(row)

    def random_point(self):
        """Return a random location coordinate on the grid."""
        return (randint(0,self.rows-1), randint(0,self.columns-1))

    def offlimit(self, location):
        """Given an (r, c) location tuple, set a cell of the
        grid to 'X' which means the robot may not step on it."""
        # Don't allow the origin or the exit to be off-limits
        if location == (0,0) or location == (self.rows-1, self.columns-1):
            return
        self.grid[location[0]][location[1]] = 'X'

    def ok_spot(self, location):
        """Check if a given (r, c) location is ok to move to."""
        if (0 <= location[0] < self.rows and
            0 <= location[1] < self.columns and
            self.grid[location[0]][location[1]] == '.'):
            return True
        return False

    def print(self):
        """Print the grid."""
        for row in self.grid:
            print(''.join(row))

    def overlay(self, path):
        """Print the grid with a path overlaid"""
        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                if (i,j) in path:
                    row.append('+')
                else:
                    row.append(self.grid[i][j])
            print(''.join(row))

class Robot(object):
    """A robot that lives on a grid and wants to find the exit."""

    def __init__(self, grid):
        """Place the robot on the grid at location 0,0"""
        self.grid = grid
        self.r = 0
        self.c = 0
        self.path = None

    def valid_moves(self, location = None):
        """Return a list of valid moves from a given location.
        If no location is given, the robot's current location is assumed."""
        if location is None:
            location = (self.r, self.c)
        moves = []
        # can we move down?
        if self.grid.ok_spot((location[0]+1, location[1])):
            moves.append((location[0]+1, location[1]))
        # can we move right?
        if self.grid.ok_spot((location[0], location[1]+1)):
            moves.append((location[0], location[1]+1))
        return moves

    def find_path(self, path = None):
        """Have the robot find a path to the exit."""
        # This version does a depth-first search. Simple and works ok
        # in many cases, but there are some grid layouts that result
        # in horrible performance.
        if path is None:
            path = deque([(0,0)])
        for move in self.valid_moves(path[-1]):
            path.append(move)
            if move == g.exit:
                return copy(path)
            result = self.find_path(path)
            if result:
                return result
            path.pop()
        return None

    def find_path2(self, path = None, failpoints = None):
        """Have the robot find a path to the exit."""
        # Modified version of original DFS. Uses book's suggestion
        # of tracking failed points to avoid re-evaluating them.
        # Much better performance.
        if path is None:
            path = deque([(0,0)])
        if failpoints is None:
            failpoints = set()
        for move in self.valid_moves(path[-1]):
            if move in failpoints:
                continue
            path.append(move)
            if move == g.exit:
                return copy(path)
            result = self.find_path2(path, failpoints)
            if result:
                return result
            failpoints.add(path.pop())
        return None

    def find_path_bfs(self, from_loc = None, to_loc = None, seen = None, prior_level = None, path = None, depth=0):
        """Does a breadth-first search for each new set of cells:
         ex: which cells can I reach in 3 moves? 4 moves? etc
         I submit that this would get a shorter path than the book solution IF there
         were more degrees of freedom in the possible moves, and more blockages
         on the grid forcing backtracking around blocks.  Not as fast
         for this particular problem, though."""
        if path is None:
            path = deque()  # so we can append to the front easily
        if from_loc is None:
            from_loc = (self.r, self.c)
        if to_loc is None:
            to_loc = self.grid.exit
        if seen is None:
            seen = {from_loc}
        if prior_level is None:
            prior_level = [from_loc]
        this_level = list()       # record the new cells we could reach
        this_level_from = list()  # record which cell brought us to each
        end_found = False
        # print(f"{depth} -- {prior_level}")
        for loc in prior_level:
            if end_found:
                break
            for m in self.valid_moves(loc):
                if m in seen:
                    continue
                seen.add(m)
                this_level.append(m)
                this_level_from.append(loc)
                if m == to_loc:
                    end_found = True
                    path.appendleft(m)
                    break
        # now process the next lower level
        if not end_found:
            self.find_path_bfs(from_loc, to_loc, seen, prior_level = this_level, path = path, depth=depth+1)
        # now start backing out. If path is not empty, a path to the end exists.
        # Record the place prior to the most recent element in our path.
        if path:
            path.appendleft(this_level_from[this_level.index(path[0])])
        return path

    def get_path(self, to_loc, path=None, failedpoints=None):
        """Version of get_path from book solution"""
        # inits
        if path is None:
            path = list()
        if failedpoints is None:
            failedpoints = set()
        # if out of bounds or not available, return
        if not self.grid.ok_spot(to_loc):
            return False
        # if we've already visited this cell, return
        if to_loc in failedpoints:
            return False
        isAtOrigin = to_loc == (0,0)
        # if there's a path from start to my current location, add my loc
        if (isAtOrigin
            or self.get_path((to_loc[0],to_loc[1]-1), path, failedpoints)
            or self.get_path((to_loc[0]-1,to_loc[1]), path, failedpoints)):
            path.append(to_loc)
            return path
        failedpoints.add(to_loc)
        return False

if __name__ == "__main__":
    # let's have a race.
    print('Expect this to run for about 30 seconds.')
    import time
    g = Grid(100,100)
    obstacles = [(0, 63), (0, 74), (1, 30), (2, 1), (3, 1), (3, 22), (3, 26),
                 (4, 20), (4, 62), (8, 9), (8, 12), (8, 89), (9, 31), (10, 72),
                 (11, 13), (11, 33), (12, 9), (12, 52), (13, 0), (13, 14),
                 (13, 59), (14, 2), (15, 58), (16, 89), (17, 13), (17, 69),
                 (18, 44), (18, 81), (19, 35), (19, 40), (19, 45), (19, 59),
                 (20, 8), (20, 57), (20, 63), (20, 86), (21, 54), (22, 49),
                 (22, 52), (22, 81), (24, 3), (24, 4), (24, 36), (25, 58),
                 (26, 26), (26, 49), (27, 31), (27, 52), (27, 53), (28, 24),
                 (33, 84), (34, 30), (34, 74), (35, 22), (36, 36), (36, 85),
                 (36, 87), (36, 98), (38, 34), (39, 8), (39, 33), (39, 70),
                 (39, 80), (39, 89), (41, 65), (41, 70), (41, 83), (41, 93),
                 (41, 97), (43, 19), (43, 38), (43, 50), (43, 86), (43, 96),
                 (44, 49), (44, 62), (45, 61), (45, 66), (45, 77), (46, 5),
                 (46, 50), (46, 85), (47, 10), (47, 28), (47, 43), (47, 57),
                 (47, 66), (47, 85), (48, 18), (49, 7), (49, 8), (49, 53),
                 (49, 60), (50, 54), (50, 61), (51, 15), (51, 84), (52, 41),
                 (52, 68), (52, 81), (53, 17), (53, 81), (54, 5), (54, 40),
                 (54, 67), (54, 80), (56, 66), (57, 36), (57, 52), (57, 85),
                 (58, 25), (58, 81), (61, 17), (61, 82), (62, 99), (63, 18),
                 (63, 67), (64, 11), (65, 27), (66, 4), (66, 83), (67, 73),
                 (68, 6), (68, 77), (68, 90), (69, 27), (69, 84), (70, 72),
                 (71, 41), (72, 1), (72, 38), (72, 56), (74, 9), (74, 16),
                 (74, 48), (75, 9), (76, 68), (76, 82), (76, 88), (77, 42),
                 (79, 8), (79, 91), (80, 25), (80, 40), (81, 31), (81, 56),
                 (82, 22), (82, 48), (82, 68), (82, 90), (83, 32), (83, 36),
                 (83, 69), (83, 75), (84, 48), (84, 91), (85, 17), (85, 19),
                 (85, 41), (85, 72), (86, 66), (87, 72), (87, 88), (88, 25),
                 (88, 41), (88, 55), (88, 78), (89, 29), (90, 1), (90, 9),
                 (90, 18), (90, 76), (91, 4), (91, 84), (92, 0), (92, 29),
                 (92, 56), (93, 2), (93, 10), (93, 52), (93, 63), (94, 29),
                 (94, 64), (94, 81), (94, 96), (95, 54), (95, 59), (95, 80),
                 (96, 40), (96, 44), (96, 58), (97, 24), (97, 53), (98, 76),
                 (98, 90), (99, 8), (99, 30), (99, 83)]
    for obstacle in obstacles:
        g.offlimit(obstacle)
    rob = Robot(g)
    start = time.time()
    path1 = rob.find_path()
    t1 = time.time()
    path2 = rob.find_path2()
    t2 = time.time()    
    path3 = rob.find_path_bfs()
    t3 = time.time()
    path4 = rob.get_path(g.exit)
    t4 = time.time()
    print("original  = {}".format(t1-start))
    print("original2 = {}".format(t2-t1))    
    print("bfs       = {}".format(t3-t2))
    print("book      = {}".format(t4-t3))

    g.overlay(path2)

    

        


