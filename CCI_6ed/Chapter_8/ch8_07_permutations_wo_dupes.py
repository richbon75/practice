"""Write a method to compute all permutations of a string of unique characters."""

def permute(A, prefix = '', result = None):
    """Compute all permutations of a string of unique characters."""
    if result is None:
        result = list()
    if not A:
        result.append(prefix)
    for i in range(len(A)):
        permute(A[0:i] + A[i+1:], prefix + A[i], result)
    return result

if __name__ == "__main__":
    result = permute('ABCD')
    print(result)

