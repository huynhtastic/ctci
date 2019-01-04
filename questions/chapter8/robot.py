"""
Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with
r rows and c columns.  The robot can only move in two directions, right and
down, but certain cells are "off limits" such that the robot cannot step on
them. Design an algorithm to find a path for the robot from the top left to the
bottom right.
"""

grid = [['o','o','o'],
        ['o','o','o'],
        ['x','x','o']]

def robot(x, y, r, c, grid, path=[]):
    if x >= c or y >= r: return False
    if grid[x][y] == 'x': return False
    if len(path) == r+c-2: return path

    return robot(x+1, y, r, c, grid, path + ['d']) or robot(x, y+1, r, c, grid, path + ['r'])
