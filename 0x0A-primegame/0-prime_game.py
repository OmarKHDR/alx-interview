#!/usr/bin/python3
""" Hello gamers
"""


def isWinner(x, nums):
    """ IDK WHY i have that x
    """
    ben = 0
    maria = 0
    if x < 1:
        return None
    for n in range(x):
        if nums[n] < 2:
            ben += 1
            continue
        arr = [x for x in range(1, nums[n] + 1)]
        i = 1
        while i <= nums[n]:
            if len(arr) == 1:
                if i % 2 != 0:
                    ben += 1
                else:
                    maria += 1
                break
            arr = play(arr)
            i += 1
    return 'Ben' if ben > maria else 'Maria'


def play(arr):
    """ Easy mode: on
    """
    p = arr[1]
    return list(filter(lambda x: (x % p != 0), arr))
