import time
replacements = []
molecule = ''

f = open('a19_input.txt', 'r')
for line in f:
    line = line.strip()
    if '=>' in line:
        element = line.split()
        replacements.append((element[0],element[2]))
    else:
        molecule = line
f.close()

def find_all_reversals(molecule):
    reversals = []
    # (oldtext, reversedtext, location)
    for replacement in replacements:
        start = molecule.find(replacement[1], 0)
        while start != -1:
            reversals.append(tuple([replacement[1], replacement[0], start]))
            start = molecule.find(replacement[0], start+1)
    return reversals

def apply_reversal(reversal, molecule):
    #reversal = (oldtext, reversedtext, location)
    return (molecule[0:reversal[2]] + reversal[1] +
            molecule[reversal[2]+len(reversal[0]):])

shortest_depth = 1000000000000000
print('Starting!')
start_time = time.time()
seen_it = set()
progress = len(find_all_reversals(molecule))

def shrink(molecule, depth = 0):
    # print(len(molecule), depth)
    global seen_it
    if molecule == 'e':
        # Path to 'e' FOUND!
        global shortest_depth
        if depth < shortest_depth:
            shortest_depth = depth
            print('{}  New shortest depth found: {}'.format(time.time()-start_time, depth))
        return None
    if depth > shortest_depth:
        # We've gone too far, go no further.
        return None
    if 'e' in molecule:
        # Went to 'e' too early!  Go no further.
        return None
    tested = 0
    for reversal in sorted(find_all_reversals(molecule), key=lambda x: len(x[0]), reverse=True):
        test_molecule = apply_reversal(reversal, molecule)
        if test_molecule in seen_it:
            continue
        seen_it.add(test_molecule)
        shrink(test_molecule, depth+1)
        seen_it.remove(test_molecule)
        if not depth:
            tested += 1
            print('Progress: {}/{}    Elapsed: {}'.format(tested, progress, time.time()-start_time))

shrink(molecule)
print('ALL DONE!')
print(time.time() - start_time)




