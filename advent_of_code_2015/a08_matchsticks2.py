
code_char = 0
expanded_char = 0

f = open('a08_input.txt', 'r')
for line in f:
    line = line.strip()
    code_char += len(line)
    expanded_char += len(line) + line.count('"') + line.count('\\') + 2
f.close()

print('difference = ', expanded_char - code_char)
