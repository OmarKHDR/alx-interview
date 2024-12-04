#!/usr/bin/python3
"""THis is supposed to be documentation
"""


def island_perimeter(grid):
    """ THisis Doc DOc ODc
    """
    perimeter = 0
    for row in range(len(grid)):
        for ele in range(len(grid[row])):
            if grid[row][ele] == 1:
                perimeter += 4
                if row > 0:
                    perimeter -= grid[row-1][ele]
                if ele > 0:
                    perimeter -= grid[row][ele-1]
                if row < (len(grid) - 1):
                    perimeter -= grid[row+1][ele]
                if ele < (len(grid[row]) - 1):
                    perimeter -= grid[row][ele+1]
    return perimeter
