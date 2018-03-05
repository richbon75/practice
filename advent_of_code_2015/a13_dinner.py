
guests = {}

f = open('a13_input.txt','r')
for line in f:
    element = line.strip().strip('.').split(' ')
    if element[0] not in guests:
        guests[element[0]] = {}
    guests[element[0]][element[10]] = int(element[3]) * (-1 if element[2] == 'lose' else 1)
f.close()

# print(guests)

def score_seat(table, seat):
    happiness = guests[table[seat]][table[seat-1]] # correctly warps for seat=0
    happiness += guests[table[seat]][table[(seat+1)%len(table)]]
    return happiness

def score_table(table):
    happiness = 0
    for i in range(len(table)):
        happiness += score_seat(table, i)
    return happiness

def permute_guests(seated, remaining_guests):
    maxscore = -1000000
    if remaining_guests:
        for guest in remaining_guests:
            seated.append(guest)
            maxscore = max(maxscore, permute_guests(seated, [x for x in remaining_guests if x != guest]))
            seated.pop()
        return maxscore
    else:
        return score_table(seated)

list_of_guests = list(guests)

print('Best possible score: ', permute_guests(['Alice'], [x for x in list_of_guests if x != 'Alice']))
      
