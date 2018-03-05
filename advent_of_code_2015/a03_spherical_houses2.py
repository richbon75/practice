
class Neighborhood(object):
    def __init__(self):
        self.houses = {}
        self.current_house = (0, 0)
        self.houses[self.current_house] = 1
        self.distinct_houses_visited = 1
        self.gifts_delivered = 0

    def visit_house(self, direction):
        if direction == '^':
            self.current_house = (self.current_house[0], self.current_house[1]+1)
        elif direction == 'v':
            self.current_house = (self.current_house[0], self.current_house[1]-1)
        elif direction == '<':
            self.current_house = (self.current_house[0]-1, self.current_house[1])
        elif direction == '>':
            self.current_house = (self.current_house[0]+1, self.current_house[1])
        else:
            raise(ValueError, 'unknown direction "{}"'.format(direction))
        if not self.houses.get(self.current_house, 0):
            self.distinct_houses_visited += 1
            self.houses[self.current_house] = 1
        else:
            self.houses[self.current_house] += 1

hood = Neighborhood()
robohood = Neighborhood()
toggle = True
f = open('a03_input.txt')
for line in f:
    for char in line.strip():
        if toggle:
            hood.visit_house(char)
            toggle = False
        else:
            robohood.visit_house(char)
            toggle = True        
f.close

santa_houses = set({x for x in hood.houses})
total_houses = santa_houses.union({x for x in robohood.houses})
print('Distinct houses = ', len(total_houses))

        
            
            
