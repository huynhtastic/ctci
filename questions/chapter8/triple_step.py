"""
Triple Step: A child is running up a staircase with n steps and can hop either
1 step, 2 steps, or 3 steps at a time. Implement a method to count how many
possible ways the child can run up the stairs.
"""

def triple_step(n):
    '''
    O(2^n)
    '''
    if n == 0 or n == 1: return 1
    if n == 2: return 2

    count = 0

    for i in range(1,4):
        if n >= i:
            count += triple_step(n-i)

    return count

def trip_step(n, memo={}):
    if n == 0 or n == 1: return 1
    if n == 2: return 2

    count = 0

    for i in range(1,4):
        temp = n - i
        if temp >= 0:
            if temp in memo:
                count += memo[temp]
            else:
                memo[temp] = trip_step(temp, memo)
                count += memo[temp]

    return count
