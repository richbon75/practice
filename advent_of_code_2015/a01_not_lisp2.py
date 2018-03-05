f = open('a01_input.txt')
up = 0
down = 0
for line in f:
    for char in line:
        if char == '(':
            up += 1
        elif char == ')':
            down += 1
        if up - down == -1:
            print('Basement reached at step ', up + down)
        
f.close()
print('Floor: ', up - down)
