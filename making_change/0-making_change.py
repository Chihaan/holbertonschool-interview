#!/usr/bin/python3
"""Making change"""


def makeChange(coins, total):
    """determine the fewest number of coins needed"""
    if total <= 0:
        return 0

    dp = [0] + [float('inf')] * total

    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount and dp[amount - coin] + 1 < dp[amount]:
                dp[amount] = dp[amount - coin] + 1

    return dp[total] if dp[total] != float('inf') else - 1

