#!/usr/bin/python3
"""THis is supposed to be documentation
"""
from typing import List


def island_perimeter(grid:List[List[int]]):
    perimeter: int = 0
    for row in range(len(grid)):
        for ele in range(len(grid[row])):
            # print(grid[row][ele], end="")
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

