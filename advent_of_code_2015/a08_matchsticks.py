
code_char = 0
mem_char = 0

f = open('a08_input.txt', 'r')
for line in f:
    line = line.strip()
    code_char += len(line)
    mem_char += len(eval(line))
f.close()

print('difference = ', code_char - mem_char)
