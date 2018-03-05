f = open('a01_input.txt')
up = 0
down = 0
for line in f:
    for char in line:
        if char == '(':
            up += 1
        elif char == ')':
            down += 1
f.close()
print('Floor: ', up - down)
