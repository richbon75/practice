
class Grid(object):
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [([0]*cols) for x in range(rows)]
        self.stage_toggles = []

    def lookup(self, rowcol):
        # rowcol is a (row, col) tuple
        if (rowcol[0] < 0 or rowcol[0] >= self.rows or
            rowcol[1] < 0 or rowcol[1] >= self.cols):
            return 0
        return self.grid[rowcol[0]][rowcol[1]]

    def toggle(self, rowcol):
        self.grid[rowcol[0]][rowcol[1]] ^= 1

    def set(self, rowcol):
        self.grid[rowcol[0]][rowcol[1]] = 1

    def stage_toggle(self, rowcol):
        self.stage_toggles.append(rowcol)

    def update_frame(self):
        for cell in self.stage_toggles:
            self.toggle(cell)
        self.stage_toggles = []

    def ons(self):
        # how many are on?
        total = 0
        for row in self.grid:
            total += sum(row)
        return total

    def count_neighbors(self, rowcol):
        return (self.lookup([rowcol[0]-1, rowcol[1]-1]) +
                self.lookup([rowcol[0]-1, rowcol[1]]) +
                self.lookup([rowcol[0]-1, rowcol[1]+1]) +
                self.lookup([rowcol[0], rowcol[1]-1]) +
                self.lookup([rowcol[0], rowcol[1]+1]) +
                self.lookup([rowcol[0]+1, rowcol[1]-1]) +
                self.lookup([rowcol[0]+1, rowcol[1]]) +
                self.lookup([rowcol[0]+1, rowcol[1]+1]))

    def print(self):
        for row in self.grid:
            output = ''
            for cell in row:
                if not cell:
                    output += '.'
                else:
                    output += '#'
            print(output)

    def cycle(self):
        for r, row in enumerate(self.grid):
            for c, cell in enumerate(row):
                neighbors = self.count_neighbors([r,c])
                if not cell and neighbors == 3:
                    self.stage_toggle(tuple([r,c]))
                elif cell and (neighbors < 2 or neighbors > 3):
                    self.stage_toggle(tuple([r,c]))
        self.update_frame()

    def pcycle(self):
        self.cycle()
        self.print()                    

g = Grid(100,100)

f = open('a18_input.txt', 'r')
for row, line in enumerate(f):
    for col, char in enumerate(list(line.strip())):
        if char == '#':
            g.set((row, col))
f.close()

for _ in range(100):
   g.cycle()
print('Number on: ', g.ons())


        
        
