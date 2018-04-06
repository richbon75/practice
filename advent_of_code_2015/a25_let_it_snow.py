
def code_at(r,c):
    """Given a row and column, what number code is there?
    ex: code_at(1,1) = 1, code_at(2,1) = 2, code_at(1,2) = 3
    """
    code = 1
    inc = 1
    while r > 1:
        code += inc
        inc += 1
        r -= 1
    inc += 1
    while c > 1:
        code += inc
        inc += 1
        c -= 1
    return code


def diagonal_row(code):
    """Find the diagonal row that the value is in."""
    first_val = 1
    inc = 1
    diag_row = 1
    while first_val <= code-inc:
        first_val += inc
        inc += 1
        diag_row += 1
    return diag_row
    
def whereis(code):
    """Return the (r, c) location for a given code.
    ex: whereis(1) = (1,1), whereis(14) = (2,4)
    """
    # find the diagonal row for the number
    diag_row = diagonal_row(code)
    # what's the last number in that diagonal row?
    last = last_in_drow(diag_row)
    # row is how many less than the last (plus one)
    row = last - code + 1
    # col
    col = diag_row - (last - code)
    return (row, col)

def last_in_drow(drow):
    """Calculate the last number in the diagonal row."""
    return ((drow + 1)**2 - (drow + 1))//2

def code_value(code):
    if code < 1:
        return None
    current_code = 1
    current_value = 20151125
    while current_code < code:
        current_code += 1
        current_value = (current_value * 252533) % 33554393
    return current_value

# which code do I need?
code = code_at(2981, 3075)
print('Code = {}'.format(code))
# here's the code
value = code_value(code)
print('Value = {}'.format(value))


