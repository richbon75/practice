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
        # can we move right?
        if self.grid.ok_spot((location[0], location[1]+1)):
            moves.append((location[0], location[1]+1))
        # can we move down?
        if self.grid.ok_spot((location[0]+1, location[1])):
            moves.append((location[0]+1, location[1]))
        return moves

    def find_path(self, path = None):
        """Have the robot find a path to the exit."""
        # This version does a depth-first search. Simple and works ok
        # in most cases, but there are some grid layouts that could result
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

    def find_path_better(self, from_loc = None, to_loc = None, seen = None, prior_level = None, path = None, depth=0):
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
            self.find_path_better(from_loc, to_loc, seen, prior_level = this_level, path = path, depth=depth+1)
        # now start backing out. If path is not empty, a path to the end exists.
        # Record the place prior to the most recent element in our path.
        if path:
            path.appendleft(this_level_from[this_level.index(path[0])])
        return path

# TODO:  Rewrite pathfinder to go from back to front - performance
# of this pathfinder is not great for certain blockage locations.

if __name__ == "__main__":
    # Create the grid
    g = Grid(15, 30)
    # Make a bunch of obstacles
    for _ in range(30):
        g.offlimit(g.random_point())
    # Print the grid
    g.print()
    print('\n' + ('=' * 25) + '\n')
    # See if our robot can find a path through it.
    # If so, print out the path.
    rob = Robot(g)
    path_out = rob.find_path()
    if path_out:
        g.overlay(path_out)
    else:
        print('No path found.')
    better_path_out = rob.find_path_better()
    print(better_path_out)
    if better_path_out:
        g.overlay(better_path_out)
