
def isSubstring(test, target):
    # Per the instructions, this method determines if test
    # is a substring of target
    return bool(test in target)

def isRotation(test, target):
    # determine if target is a rotation of test,
    # using only one call to isSubstring
    if len(test) != len(target):
        return False
    return isSubstring(test, target+target)

if __name__ == "__main__":
    print(isRotation('waterbottle','erbottlewat'))
    
    
