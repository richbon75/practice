
def stringcrement(sequence):
    letters = list(sequence)
    for x in range(len(letters)):
        char = letters[-1-x]
        char = ord(char)+1
        if char > 122:
            char = 97
            letters[-1-x] = chr(char)
            if x == len(letters)-1:
                letters = ['a'] + letters
        else:
            letters[-1-x] = chr(char)
            break
    return ''.join(letters)

def rule0(sequence):
    if len(sequence) == 8:
        return True
    return False

def rule1(sequence):
    for x in range(2, len(sequence)):
        if (ord(sequence[x-1]) - ord(sequence[x-2]) == 1 and
            ord(sequence[x]) - ord(sequence[x-1]) == 1):
            return True
    return False

def rule2(sequence):
    if 'i' in sequence or 'o' in sequence or 'l' in sequence:
        return False
    return True

def rule3(sequence):
    found = 0
    last_found = ''
    for x in range(1, len(sequence)):
        if (sequence[x-1] == sequence[x] and sequence[x] != last_found):
            found += 1
            last_found = sequence[x]
            if found == 2:
                return True
    return False

def is_valid(sequence):
    return (rule0(sequence) and rule1(sequence) and rule2(sequence) and rule3(sequence))

sequence = 'hepxxyzz'
while True:
    sequence = stringcrement(sequence)
    if is_valid(sequence):
        print('Answer: ', sequence)
        break



            

