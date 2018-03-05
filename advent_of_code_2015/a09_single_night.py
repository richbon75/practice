

legs = {}
all_places = set()

f = open('a09_input.txt', 'r')
for line in f:
    element = line.strip().split()
    all_places = all_places.union([element[0], element[2]])
    if element[0] not in legs:
        legs[element[0]] = {}
    legs[element[0]][element[2]] = int(element[4])
    if element[2] not in legs:
        legs[element[2]] = {}
    legs[element[2]][element[0]] = int(element[4])
f.close()

shortest_path = None
shortest_found_distance = 1000000

def paths_from_place(visited, visited_score):
    global legs
    global shortest_found_distance
    global possible_paths
    # print(visited, visited_score)
    if visited[-1] not in legs:
        return
    for next_place in [place for place in legs[visited[-1]] if place not in visited]:
        # print('next_place = ', next_place)
        next_cost = legs[visited[-1]][next_place]
        visited_score += next_cost
        visited.append(next_place)
        if len(visited) == 8:
            if visited_score < shortest_found_distance:
                print('New shortest path found: ', visited, visited_score)
                shortest_found_distance = visited_score
                shortest_path = visited[:]
        else:
            paths_from_place(visited, visited_score)
        visited_score -= next_cost
        visited.pop()

for place in all_places:
    paths_from_place([place], 0)

print('Shortest distance: ', shortest_path)



    
