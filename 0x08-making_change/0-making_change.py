#!/usr/bin/python3
"""
An optimized solution for the coin change
problem using dynamic programming
with space complexity reduced to O(amount).
"""

def makeChange(coins, amount):
    """We use a large number to represent infinity (unreachable state)
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make amount 0

    # Iterate through all coin denominations
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1
