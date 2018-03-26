"""Implement an algorithm to print all valid (e.g., properly opened and closed)
combinations of n pairs of parentheses.
EXAMPLE
Input: 3
Output: ((())), (()()), (())(), ()(()), ()()()
"""

def parens(n, leading=None, closing=None):
    """Print all valid combinations of n pairs of parentheses.
    Each next parenthesis either goes inside or outside the enclosing
    parentheses."""
    if leading is None:
        leading = ''
    if closing is None:
        closing = ''
    if n == 0:
        print(leading + closing)
        return
    # We have two places to place our parens - inside or outside.
    parens(n-1, leading+'(', ')'+closing)
    if leading != '' or closing != '':
        parens(n-1, leading+closing+'(', ')')
if __name__ == "__main__":
    parens(3)

    
