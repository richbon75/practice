
def is_permutation(first, second):
    # Check if one string is a permutation of the other
    # Sort is O(Nlog(N))
    first_s = ''.join(sorted(first))
    second_s = ''.join(sorted(second))
    if first_s == second_s:
        return True
    return False

def is_permutation_dict(first, second):
    # Use dictionary hash tables. O(N) time
    if len(first) != len(second):
        return False
    f_dict = {}
    for char in first:
        f_dict[char] = f_dict.get(char,0) + 1
    s_dict = {}
    for char in second:
        s_dict[char] = s_dict.get(char,0) + 1
    if f_dict == s_dict:
        return True
    return False

from collections import Counter

def is_permutation_count(first, second):
    # A slicker version using Counter (a dict subclass) O(N)
    # Code is simpler and countdown uses half the space.
    if len(first) != len(second):
        return False
    letters = Counter()
    for char in first:
        letters[char] += 1
    for char in second:
        if letters[char] == 0:
            return False
        letters[char] -= 1
    return True

