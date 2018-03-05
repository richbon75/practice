
def one_away(first, second):
    # runs in O(N) time
    if abs(len(first) - len(second)) > 1:
        return False
    if len(first) == len(second):
        # only valid change here can be one replacement
        diffs = 0
        for i, char in enumerate(first):
            if char != second[i]:
                if diffs > 0:
                    return False
                diffs += 1
        return True
    if len(second) > len(first):
        # swap so the longest is first
        first, second = second, first
    # only valid change here can be skipping one letter of the longer
    diffs = 0
    for i, char in enumerate(second):
        if char != first[i + diffs]:
            if diffs or char != first[i+1]:
                return False
            diffs += 1
    return True
