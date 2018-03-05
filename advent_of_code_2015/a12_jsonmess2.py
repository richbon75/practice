import json

f = open('a12_input.txt', 'r')
data = f.read()
f.close()
data = json.loads(data.strip())

def diveinto(x):
    total = 0
    if type(x) is int:
        total += x
    elif type(x) is str:
        pass #ignore strings
    elif type(x) is list:
        for y in x:
            total += diveinto(y)
    elif type(x) is dict:
        for key in x:
            if x[key] == 'red':
                return 0
            total += diveinto(x[key])
    else:
        print('Unknown type encountered: {} value: {}'.format(type(x), x))
    return total

print(diveinto(data))


            
