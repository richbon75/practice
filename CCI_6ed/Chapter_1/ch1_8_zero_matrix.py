
def zero_matrix(matrix):
    # Performs in O(N) time.
    # Even on a matrix with full zeroes, every cell is only updated twice.
    # Space is O(N) (will use up to N + (W+H) if every cell is zero)
    height = len(matrix)
    width = len(matrix[0])
    # store the rows and cols to be zeroed as sets (no dupes)
    zrows = set()
    zcols = set()
    # find the locations of any zero elements
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

if __name__ == "__main__":
    from pprint import pprint
    m = [[]]
    pprint(zero_matrix(m))
    m = [['A','B','C'],['D',0,'E'],['F','G','H']]
    pprint(zero_matrix(m))
    m = [['A','B','C','D','E','F'],
         ['G','H','I','J',None,'L'],
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
    
