
sue = list()

f = open('a16_input.txt','r')
for line in f:
    this_sue = {}
    element = line.strip().split()
    this_sue['number'] = element[1].strip(':')
    this_sue[element[2].strip(':')] = int(element[3].strip(','))
    this_sue[element[4].strip(':')] = int(element[5].strip(','))
    this_sue[element[6].strip(':')] = int(element[7].strip(','))
    sue.append(this_sue)
f.close()

what_i_know = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1}

possible_sues = []
for i, s in enumerate(sue):
    possible = True
    for known in what_i_know:
        if known in s:
            if what_i_know[known] != s[known]:
                possible = False
    if possible:
        possible_sues.append(s)

print('Send thank you to Aunt Sue: {}'.format(possible_sues))
