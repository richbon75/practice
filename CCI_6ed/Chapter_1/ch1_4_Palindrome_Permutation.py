
# Same as checking a palindrome, but ignore spaces

from collections import Counter

def palindrome(first, second):
    letters = Counter()
    flen = 0
    slen = 0
    for char in first:
        if char != ' ':
            letters[char] += 1
            flen += 1
    for char in second:
        if char != ' ':
            letters[char] -= 1
            if letters[char] < 0:
                return False
            slen += 1
    if flen != slen:
        return False
    return True

        
