"""Search in Rotated Array: Given a sorted array of n integers that has
been rotated an unknown number of times, write code to find an element in
the array. You may assume that the array was originally sorted in increasing
order.
EXAMPLE
Input:find 5 in [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
Output: 8 (the index of 5 in the array)"""

# Thoughts:
# * At least one half of this array is still in sorted order,
#   we can figure out which half by comparing the center element against
#   the ends.
# * If the first element is < center, then that half is still sorted,
#   if the last  element is > center, then that half is still sorted.
# * If the target value is in the sorted section, run binary search in
#   that section.  Else, split the unsorted half and see which half of that
#   is sorted, recurse.

def binary_search(values, target, start = None, end = None):
    start = start if start is not None else 0
    end = end if end is not None else len(values)-1
    if start > end:
        return None
    center = (start + end) // 2
    print (f'BS - {start} {center} {end}')
    if values[center] == target:
        return center
    if values[center] > target:
        return binary_search(values, target, start, center-1)
    return binary_search(values, target, center+1, end)

def rotated_search(values, target, start = None, end = None):
    start = start if start is not None else 0
    end = end if end is not None else len(values)-1
    if start > end:
        return None
    center = (start + end) // 2
    print (f'RS - {start} {center} {end}')    
    if values[center] == target:
        return center
    if values[start] <= target and target <= values[center]:
        # target to left, and left is sorted
        return binary_search(values, target, start, center-1)    
    if values[center] <= target and target <= values[end]:
        # target to right, and right is sorted
        return binary_search(values, target, center+1, end)
    if values[start] <= values[center]:
        # left is sorted, but value isn't there, check right
        return rotated_search(values, target, center+1, end)
    else: # right is sorted, but value isn't there, check left
        return rotated_search(values, target, start, center-1)

def rotate(values, n):
    return values[n:] + values[0:n]
        
test = [1, 3, 4, 5, 7, 10, 14, 15, 16, 19, 20, 25]

# test by trying all possible rotations

for i in range(0, len(test)):
    vals = rotate(test, i)
    print(vals)
    result = rotated_search(vals, 5)
    print(f'result = {result}  expected_value = {vals.index(5)}')
    assert result == vals.index(5), 'Did not achieve expected result.'

