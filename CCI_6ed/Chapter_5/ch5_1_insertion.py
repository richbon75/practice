"""Bit manipulation
You are given two 32-bit numbers, N and M, and two bit positions, i and j.
Write a method to insert M into N such that M starts at bit j and ends at bit i.
You can assume that the bits j through i have enough space to fit all of M.
That is, if M = 10011, you can assume that there are at least 5 bits between j
and i. You would not, for example, have j = 3 and i = 2, because M could not
fully fit between bit 3 and bit 2.
EXAMPLE
Input:  N = 10000000000, M = 10011, i 2, j 6
Output: N = 10001001100
"""

# Looks like we're just overwriting the bits in positions j to i.
# Note: Because of the way integers work in Python (no fixed byte length)
# you can't make a one step "AND" mask of zeros where you want to clear
# values and 1s everywhere else, because the "everywhere else" space is
# effectively infinite. So I'll do it in a two-step process with a mask
# that has 1s where I want to clear values and 0s "everywhere else" (since
# that's the default)

def binary_overlay(N, M, i, j):
    # make a mask
    mask = 1
    for _ in range(j-i):
        mask = (mask << 1) | 1
    mask <<= i
    # shift M to the right place
    M <<= i
    # clear out old bits. Remember - no standard bit width in Python integers
    N |= mask
    N ^= mask
    # overlay new bits
    N |= M
    return N
    
if __name__ == '__main__':
    print('{0:b}'.format(binary_overlay(0b10000000000, 0b10011, 2, 6)))

        
