
import math

def factors(x):
    facts = set()
    for i in range(1, math.floor(math.sqrt(x))+1):
        if not x % i:
            facts.add(i)
            facts.add(x // i)
    return facts

def score(x):
    return sum(factors(x)) * 10

i = 1
while score(i) < 33100000:
    i += 1
print('Value: {}  Score: {}'.format(i, score(i)))



    
