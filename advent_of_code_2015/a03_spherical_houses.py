
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
f = open('a03_input.txt')
for line in f:
    for char in line.strip():
        hood.visit_house(char)
f.close

print('Distinct Houses: ', hood.distinct_houses_visited)

        
            
            
