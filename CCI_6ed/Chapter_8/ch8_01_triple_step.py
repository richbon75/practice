"""A child running up a staircase with n steps and can hop either 1 step,
2 steps, or 3 steps at a time.  Implement a method to count how many possible
ways the child can run up the stairs."""

import time

def ways_up_count(n):
    """Count how many ways the kid can climb the stairs.
    This version does it by brute force."""
    if n == 0:
        return 1
    ways = 0
    for takestep in range(1, 4):
        if takestep <= n:
            ways += ways_up_count(n-takestep)
    return ways

def ways_up_cache(n, cache = None):
    """Same idea, but with caching the answer for
    lower-number steps as it finds them to avoid re-calculating them"""
    if cache is None:
        cache = dict()
    if n == 0:
        return 1
    if n in cache:
        return cache[n]
    ways = 0
    for takestep in range(1, 4):
        if takestep <= n:
            ways += ways_up_cache(n-takestep, cache)
    cache[n] = ways
    return ways            

def ways_up_oneway(n):
    """Don't need to recurse, we just carry forward the last three steps,
    because each new step is the sum of the three previous steps."""
    if n < 1:
        return None
    p1, p2, p3 = 0, 0, 1      # base case of n == 1
    for step in range(1, n):  # don't iterate for n == 1
        p1, p2, p3 = p2, p3, p3 + p2 + p1
    return p1 + p2 + p3


if __name__ == "__main__":
    print ('Using ways_up_count()')
    steps = 25
    start = time.time()
    results = ways_up_count(steps)
    elapsed = time.time() - start
    print('{} steps {} ways.  Took {} seconds.'.format(steps, results, elapsed))

    print('Using ways_up_cache()')
    steps = 25
    start = time.time()
    results = ways_up_cache(steps)
    elapsed = time.time() - start
    print('{} steps {} ways.  Took {} seconds.'.format(steps, results, elapsed))

    print('Using ways_up_oneway()')
    steps = 25
    start = time.time()
    results = ways_up_oneway(steps)
    elapsed = time.time() - start
    print('{} steps {} ways.  Took {} seconds.'.format(steps, results, elapsed))
