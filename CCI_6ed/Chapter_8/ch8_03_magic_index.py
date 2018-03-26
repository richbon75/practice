"""A magic index in an array A[0...n-1] is defined to be an index such
that A[i] = i. Given a *sorted array* of distinct integers, write a method
to find a magic index, if one exists, in array A.
FOLLOW UP
What if the values are not distinct?"""

def find_magic_index_simple(A):
    """Simple way to find a magic index, runs in O(N)"""
    for i in range(len(A)):
        if A[i] == i:
            return i
    return None

def find_magic_index_fancy(A):
    """This version finds a magic index in O(logN) by splitting
    the search space in half each iteration. Assumes elements
    are distinct."""
    left_index = 0
    right_index = len(A)-1
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        last_mid = mid_index
        if mid_index == A[mid_index]:
            return mid_index
        if mid_index > A[mid_index]:
            left_index = mid_index+1
        else:
            right_index = mid_index-1
    return None

def find_magic_index_dupes(A, left_index = None, right_index = None):
    """This version takes duplicate values into account by splitting
    the search space into left and right sides, shortening where possible.
    Also, this version is recursive rather than iterative.
    For distinct lists, not much better than O(N) version."""
    if left_index is None:
        left_index, right_index = 0, len(A)-1
    if left_index > right_index:
        return None
    mid_index = (left_index + right_index) // 2
    if mid_index == A[mid_index]:
        return mid_index
    # search left side
    left_magic = find_magic_index_dupes(A, left_index, min(mid_index-1, A[mid_index]))
    if left_magic is not None:
        return left_magic
    # search right side
    right_magic = find_magic_index_dupes(A, max(mid_index+1, A[mid_index]), right_index)
    if right_magic is not None:
        return right_magic
    return None

if __name__ == "__main__":
    print ('Lists without dupes')
    from random import randint
    magic = randint(0, 999)
    print(f"magic={magic}")
    A = [None] * 1000
    A[magic] = magic
    for i in range(0, magic):
        A[i] = i-1
    for i in range(magic+1, 1000):
        A[i] = i+1
    print(find_magic_index_simple(A))
    print(find_magic_index_fancy(A))
    print(find_magic_index_dupes(A))

    # What if elements are not distinct?
    print ('List with dupes')
    B = [-10, -5, 2, 2, 2, 3, 4, 8, 9, 12, 13]
    print(find_magic_index_simple(B))
    print(find_magic_index_fancy(B)) # may not find it
    print(find_magic_index_dupes(B))
    
