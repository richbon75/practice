
registers = {}
operations = []
# Overriding wire b to 16076
registers['b'] = 16076

class Operation(object):
    def __init__(self, op, in1, in2, dest):
        self.op = op
        self.in1 = in1
        self.in2 = in2
        self.dest = dest
        if self.op in ('NOT', 'SET'):
            self.in2 = 0
            self.in2_val = 0

    def __str__(self):
        return '{} {} {} -> {}'.format(self.op, self.in1, self.in2, self.dest)

    def decode(self, x):
        try:
            return int(x)
        except ValueError:
            global registers
            return registers.get(x, None)

    def operate(self):
        """Try to take the inputs and set the output."""
        if self.decode(self.dest) is not None:
            # if we've already evaluated this one, we're done with it
            return True
        if self.decode(self.in1) is not None and self.decode(self.in2) is not None:
            # If we have whate we need, perform the operation
            global registers
            if self.op == 'SET':
                registers[self.dest] = self.decode(self.in1)
            elif self.op == 'NOT': # 16 bit!
                registers[self.dest] = 65535 - self.decode(self.in1)
            elif self.op == 'AND':
                registers[self.dest] = self.decode(self.in1) & self.decode(self.in2)
            elif self.op == 'OR':
                registers[self.dest] = self.decode(self.in1) | self.decode(self.in2)
            elif self.op == 'RSHIFT':
                registers[self.dest] = self.decode(self.in1) >> self.decode(self.in2)
            elif self.op == 'LSHIFT':
                registers[self.dest] = self.decode(self.in1) << self.decode(self.in2)
            else:
                raise(ValueError, 'Unknown op {}'.format(self.op))                
            return True
        else:
            # Not enough info to perform the operation
            return False

f = open('a07_input.txt', 'r')
for line in f:
    element = line.strip().split(' ')
    if element[0] == 'NOT':
        operations.append(Operation('NOT', element[1], None, element[3]))
    elif element[1] == '->':
        operations.append(Operation('SET', element[0], None, element[2]))
    else:
        operations.append(Operation(element[1], element[0], element[2], element[4]))
f.close()

all_done = False
while not all_done:
    all_done = True
    for op in operations:
        all_done &= op.operate()

print('Value in register a: {}'.format(registers['a']))

    
                            
            
