
class Lights(object):

    def __init__(self, width, height):
        self.grid = []
        for i in range(height):
            row = []
            for j in range(width):
                row.append(0)
            self.grid.append(row)

    def turn_on(self, from_coords, to_coords):
        for i in range(from_coords[0], to_coords[0]+1):
            for j in range(from_coords[1], to_coords[1]+1):
                self.grid[i][j] = 1

    def turn_off(self, from_coords, to_coords):
        for i in range(from_coords[0], to_coords[0]+1):
            for j in range(from_coords[1], to_coords[1]+1):
                self.grid[i][j] = 0

    def toggle(self, from_coords, to_coords):
        for i in range(from_coords[0], to_coords[0]+1):
            for j in range(from_coords[1], to_coords[1]+1):
                self.grid[i][j] ^= 1

    def number_lit(self):
        lit = 0
        for row in self.grid:
            for light in row:
                lit += light
        return lit

lights = Lights(1000,1000)

f = open('a06_input.txt','r')
for line in f:
    pieces = line.strip().split(' ')
    to_coords = tuple(int(x) for x in pieces[-1].split(','))
    from_coords = tuple(int(x) for x in pieces[-3].split(','))
    instruction = ' '.join(pieces[0:-3])
    if instruction == 'turn on':
        lights.turn_on(from_coords, to_coords)
    elif instruction == 'turn off':
        lights.turn_off(from_coords, to_coords)
    elif instruction == 'toggle':
        lights.toggle(from_coords, to_coords)
    else:
        raise(ValueError, 'Unknown instruction {}'.format(instruction))
f.close()

print('Lights lit = ', lights.number_lit())

    
