"""A child running up a staircase with n steps and can hop either 1 step,
2 steps, or 3 steps at a time.  Implement a method to count how many possible
ways the child can run up the stairs."""

import time

def ways_up_count(n):
    """Count how many ways the kid can climb the stairs"""
    if n == 0:
        return 1
    ways = 0
    for takestep in range(1, 4):
        if takestep <= n:
            ways += ways_up_count(n-takestep)
    return ways

def ways_up_memo(n, cache = None):
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
            ways += ways_up_memo(n-takestep, cache)
    cache[n] = ways
    return ways            

if __name__ == "__main__":
    print ('Using ways_up_count()')
    steps = 25
    start = time.time()
    results = ways_up_count(steps)
    elapsed = time.time() - start
    print('{} steps {} ways.  Took {} seconds.'.format(steps, results, elapsed))

    print('Using ways_up_memo()')
    steps = 25
    start = time.time()
    results = ways_up_memo(steps)
    elapsed = time.time() - start
    print('{} steps {} ways.  Took {} seconds.'.format(steps, results, elapsed))

    
