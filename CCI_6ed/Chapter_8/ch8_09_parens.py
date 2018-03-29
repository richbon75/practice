"""Implement an algorithm to print all valid (e.g., properly opened and closed)
combinations of n pairs of parentheses.
EXAMPLE
Input: 3
Output: ((())), (()()), (())(), ()(()), ()()()
"""

def parens(lefts, rights = None, prefix='', results = None):
    """Return all valid combinations of n pairs of parentheses"""
    if results is None:
        results = list()
    if rights is None:
        rights = lefts  # gotta have enough rights to match the lefts
    if rights == 0:
        results.append(prefix)
        return
    # we have two options for extending our prefix:
    #   we could add a left paren (if we have any remaining)
    if lefts > 0:
        parens(lefts-1, rights, prefix + '(', results)
    #   we could also add a right paren (if we have rights > lefts)
    if rights > lefts:
        parens(lefts, rights-1, prefix + ')', results)
    return results
    
if __name__ == "__main__":
    print(parens(4))


    
