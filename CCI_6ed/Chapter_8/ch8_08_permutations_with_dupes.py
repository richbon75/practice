"""Write a method to compute all permutations of a string
whose characters are not necessarily unique. The list of
permutations should not have duplicates.
"""

def permute_distinct(A, prefix = '', result = None):
    """Compute all permutations of a string of unique characters."""
    if result is None:
        result = list()
    if not A:
        result.append(prefix)
    letters_in_this_place = set()
    for i in range(len(A)):
        if A[i] in letters_in_this_place:
            continue
        letters_in_this_place.add(A[i])
        permute_distinct(A[0:i] + A[i+1:], prefix + A[i], result)
    return result

if __name__ == "__main__":
    result = permute_distinct('ABBAC')
    print(result)
    assert len(result) == len(set(result)), 'There should be no dupes to remove.'

