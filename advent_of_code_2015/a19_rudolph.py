
replacements = []
molecule = ''
variants = set()

f = open('a19_input.txt', 'r')
for line in f:
    line = line.strip()
    if '=>' in line:
        element = line.split()
        replacements.append((element[0],element[2]))
    else:
        molecule = line
f.close()

for replacement in replacements:
    start = molecule.find(replacement[0], 0)
    while start != -1:
        variant = molecule[0:start] + replacement[1] + molecule[start+len(replacement[0]):]
        variants.add(variant)
        # print(start, replacement, variant, molecule[0:start], replacement[1], molecule[start+len(replacement[0])+1:])
        start = molecule.find(replacement[0], start+1)

print('Variants possible: ', len(variants))

        
        
    
