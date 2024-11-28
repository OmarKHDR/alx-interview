#!/usr/bin/python3
""" Doc Doc Doc Doc
"""


def findChange(coin, amount, arr):
    """ This also is documented
    """
    if amount == 0:
        return 0  # Base case: no coins needed for amount 0
    if amount < 0:
        return 1000000  # Impossible case, return a large value
    
    # If already computed for this amount, return the cached value
    if arr[amount] != 1000000:
        return arr[amount]

    # Initialize minimum coins for current amount
    mini = 1000000
    for i in coin:
        if i <= amount:  # Only consider coins less than or equal to the current amount
            res = findChange(coin, amount - i, arr)  # Recursive call
            if res != 1000000:  # Only valid result if res is not impossible
                mini = min(res + 1, mini)  # Update minimum coins
    
    # Cache the result for the current amount
    arr[amount] = mini
    return mini

def makeChange(coin, amount):
    """ This is documented for real
    """
    arr = [1000000] * (amount + 1)  # Initialize the memoization array
    res = findChange(coin, amount, arr)
    return res if res != 1000000 else -1  # Return -1 if no solution
