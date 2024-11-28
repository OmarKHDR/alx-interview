#!/usr/bin/python3
"""
Given a list of coin denominations and a target amount,
this function finds the minimum number of coins
required to make the target amount.
If it is not possible to make the amount, it returns -1.
"""


def makeChange(coins, amount):
    """Initialize the DP array with a value
    representing infinity (impossible case)
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins needed to make amount 0
    # Iterate over each coin
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    # If dp[amount] is still infinity, return -1 (impossible case)
    return dp[amount] if dp[amount] != float('inf') else -1
