
def all_unique_dict(value):
    # using a dictionary
    letters = {}
    for char in value:
        letters[char] = letters.get(char, 0) + 1
        if letters[char] > 1:
            return False
    return True

def all_unique_set(value):
    # using a set - similar to dictionary, but we don't really
    # care how many times we've seen a character, just that we've
    # seen it at least once before.
    seen = set()
    for char in value:
        if char in seen:
            return False
        seen.add(char)
    return True

def all_unique_list(value):
    # only using a list
    lastchar = ''
    for char in sorted(value):
        if char == lastchar:
            return False
        lastchar = char
    return True

