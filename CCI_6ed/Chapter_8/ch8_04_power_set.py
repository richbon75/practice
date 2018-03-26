"""Write a method to return all subsets of a set."""

"""
Initial thought: This is an n choose k problem, but summed for all k from 0 to n.

Refine: Calculation could be more efficient. Initial method re-finds
a lot of subsets we've already found as building blocks for other subsets.

Note: Yes, these are lists and not "sets" in the pythonic sense.
"""

def choose_k(A, k):
    """Get all k sets of the elements in A"""
    if k > len(A):
        return []
    if k == 0:
        return [[]]
    sets = []
    for i in range(len(A)):
        sets += [[A[i]]+s for s in choose_k(A[i+1:], k-1)]
    return sets

def all_subsets(A):
    """Sum up all subsets for k from 0 to n"""
    subsets = []
    for k in range(0, len(A)+1):
        subsets += choose_k(A, k)
    return subsets

# Second, improved version below.

def all_subsets_faster(A):
    """A faster method of finding all subsets of elements in A"""
    # The empty set is a subset of all sets.
    subsets = [[]]
    # For each element in the original set, we modify our existing set of subsets.
    # We get one version without the new element, and one version WITH the element,
    # effectively doubling the set of subsets for each element.
    for element in A:
        subsets = subsets + [s + [element] for s in subsets]
    return subsets

if __name__ == "__main__":
    A = [1,2,3,4,5]
    print(all_subsets(A))
    print('='*25)
    print(all_subsets_faster(A))

        
