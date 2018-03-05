
def two_back(x):
    lookback = [None, None]
    for char in x:
        if char == lookback[0]:
            return True
        lookback[0] = lookback[1]
        lookback[1] = char
    return False

def pairs(x):
    for i in range(0, len(x)-1):
        if x.count(x[i:i+2]) >= 2:
            return True
    return False

def is_nice(x):
    return two_back(x) and pairs(x)

nice = 0
f = open('a05_input.txt')
for line in f:
    if is_nice(line.strip()):
        nice += 1
f.close()
print('nice = ', nice)
