#!/usr/bin/python3
""" Determines which player wins the Prime Game """

def isWinner(x, nums):
    """ Function Prime Game """
    mx = max(nums)
    is_prime = [True] * (mx + 1)
    is_prime[0] = False
    is_prime[1] = False
    count = [0] * (mx + 1)
    maria = 0
    ben = 0

    for i in range(2, int(mx**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, mx + 1, i):
                is_prime[j] = False

    for i in range(1, mx + 1):
        count[i] = count[i - 1]
        if is_prime[i]:
            count[i] = count[i - 1] + 1

    for num in nums:
        if count[num] % 2 == 1:
            maria += 1
        else:
            ben += 1

    if maria > ben:
        return "Maria"
    if ben > maria:
        return "Ben"
    else:
        return None
