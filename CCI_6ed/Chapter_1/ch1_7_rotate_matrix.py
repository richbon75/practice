
from math import ceil

def rotate(matrix):
    # Rotate a matrix 90 degrees clockwise
    output = []
    if not len(matrix[0]):
        return [[]]
    for j in range(len(matrix[0])):
        out_row = []
        for i in range(len(matrix)-1,-1,-1):
            out_row.append(matrix[i][j])
        output.append(out_row)
    return output

def rotate_inplace(m):
    # Rotate a matrix 90 degrees IN PLACE
    n = len(m)
    z = n-1 # make calcs later simpler
    for i in range(ceil(n/2)-n%2):
        for j in range(ceil(n/2)):
            m[i][j], m[j][z-i], m[z-i][z-j], m[z-j][i] = \
                     m[z-j][i], m[i][j], m[j][z-i], m[z-i][z-j]
    return m
    

if __name__ == "__main__":
    print('BOO RADLEY')
    m = [[]]
    print(rotate(m))
    print(rotate_inplace(m))
    m = [['A']]
    print(rotate(m))
    print(rotate_inplace(m))
    m = [['A','B'],
         ['C','D']]
    print(rotate(m))
    print(rotate_inplace(m))
    m = [['A','B','C'],
         ['D','E','F'],
         ['G','H','I']]
    print(rotate(m))
    print(rotate_inplace(m))
    m = [['A','B','C','D'],
         ['E','F','G','H'],
         ['I','J','K','L'],
         ['M','N','O','P']]
    print(rotate(m))
    print(rotate_inplace(m))
    
    
    
