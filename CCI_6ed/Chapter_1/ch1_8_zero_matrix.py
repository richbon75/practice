
def zero_matrix(matrix):
    # Performs in O(N) time.
    # Even on a matrix with full zeroes, every cell is only updated twice.
    # Space is O(N) (will use up to N + (W+H) if every cell is zero)
    height = len(matrix)
    width = len(matrix[0])
    # store the rows and cols to be zeroed as sets (no dupes)
    zrows = set()
    zcols = set()
    # find the locations of any zero elements.
    # Explicitly checking equality to zero instead of "if not matrix[i][j]"
    # because we want this to trigger only on zeros, not None
    # or empty strings, or any other Boolean False value.
    for i in range(height):
        for j in range(width):
            if matrix[i][j]==0:
                zrows.add(i)
                zcols.add(j)
    # zero the row or column
    for i in zrows:
        matrix[i] = [0 for _ in range(width)]
    for j in zcols:
        for i in range(height):
            matrix[i][j] = 0
    return matrix

# Hint in the book suggested O(1) space requirement by using
# the first row and first column to record where zeros will go.
# Will implement that later.

if __name__ == "__main__":
    from pprint import pprint
    m = [[]]
    pprint(zero_matrix(m))
    m = [['A','B','C'],['D',0,'E'],['F','G','H']]
    pprint(zero_matrix(m))
    m = [['A','B','C','D','E','F'],
         ['G','H','I','J','K','L'],
         ['M','N','O','P','Q','R'],
         ['S','T','U','V','W','X'],
         ['Y','Z','A','B','C','D']]
    pprint(zero_matrix(m))
    m[1][4] = 0
    pprint(zero_matrix(m))
    pprint(zero_matrix(m))
    m = [['A','B','C','D','E','F'],
         ['G', 0 ,'I','J','K','L'],
         ['M' ,'N','O','P','Q','R'],
         ['S','T','U','V', 0 ,'X'],
         ['Y','Z','A','B','C','D']]
    pprint(zero_matrix(m))
    
