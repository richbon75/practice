from copy import copy
from time import time

presents = [1,3,5,11,13,17,19,23,29,31,37,41,43,47,53,59,
            67,71,73,79,83,89,97,101,103,107,109,113]
presents.reverse() # try building sets with larger values first
all_presents = presents

total_weight = sum(presents)
weight_per_container = total_weight // 4

ways = set()

fewest_pkgs = len(presents)  # initial max
best_qe = None

def calc_qe(iterable):
    x = 1
    for i in iterable:
        x *= i
    return x

def can_balance(presents, N=2, this_way = None, used = None):
    """Can a set of presents be split into N equal ways?"""
    if used is None:
        used = set()
    if this_way is None:
        this_way = set()
    wpc = sum(presents) / N
    if sum(this_way) == wpc:
        if N == 2 or can_balance(presents = list(set(all_presents).difference(this_way).difference(used)),
                                 N = N-1,
                                 used = used.union(this_way)):
            return True
    for i in range(len(presents)):
        if sum(this_way) + presents[i] > wpc:
            continue
        this_way.add(presents[i])
        if can_balance(presents[i+1:], N, used=used):
            return True
        this_way.remove(presents[i])
    return False

def ways_to_make_weight(presents, wpc, ways, this_way = None):
    global fewest_pkgs
    global best_qe
    if len(ways) > fewest_pkgs:
        return
    if this_way is None:
        outer = True
        start = time()
        this_way = set()
    else:
        outer = False
    if sum(this_way) == wpc:
        # check if remaining presents can be balanced
        if can_balance(list(set(all_presents).difference(this_way)),N=3,used=this_way):
            if len(this_way) < fewest_pkgs:
                fewest_pkgs = len(this_way)
                best_qe = calc_qe(this_way)
            if len(this_way) == fewest_pkgs and best_qe > calc_qe(this_way):
                best_qe = calc_qe(this_way)
        return
    if len(presents) == 0:
        return
    for i in range(len(presents)):
        if outer:
            print((presents[i], time() - start, len(ways), fewest_pkgs, best_qe))
            start = time()
        if sum(this_way) + presents[i] > wpc:
            continue
        this_way.add(presents[i])
        ways_to_make_weight(presents = presents[i+1:],
                            wpc = wpc,
                            ways = ways,
                            this_way = this_way)
        this_way.remove(presents[i])


ways_to_make_weight(presents = presents, wpc = weight_per_container,
                    ways = ways)

print(best_qe)



        
