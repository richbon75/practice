"""Set of stacks - make new stack when current stack reaches max height."""

from collections import deque

class SetOfStacks(object):
    """Make a new stack when current stack reaches max height.
    Should be transparent to user - push() and pop() should work
    simply as expected."""

    def __init__(self, maxheight):
        """maxheight is the maximum height of a single stack"""
        self.maxheight = maxheight
        self.stax = deque()

    def __len__(self):
        return sum([len(x) for x in self.stax])

    def push(self, value):
        """Push a value onto the set of stacks"""
        if not self.stax or len(self.stax[-1]) >= self.maxheight:
            self.stax.append(deque())
        self.stax[-1].append(value)

    def pour(self, iterable):
        """Push in lots of values"""
        for value in iterable:
            self.push(value)

    def pop(self):
        """Pop a value off the set of stacks"""
        if not self.stax:
            raise IndexError('stack empty')
        value = self.stax[-1].pop()
        self.trim()
        return value

    def pop_substack(self, i):
        """Pop a value out of a substack"""
        value = self.stax[i].pop()
        self.trim()
        return value

    def trim(self):
        """Check the tail for empty stacks, and remove them."""
        while self.stax and len(self.stax[-1]) == 0:
            self.stax.pop()

    def print(self):
        """output the SetOfStacks so we can visualize it"""
        for i, x in enumerate(self.stax):
            print('{i} : {x}'.format(i=i, x=x))

if __name__ == "__main__":
    merp = SetOfStacks(7)
    merp.pour(range(0, 55))
    merp.print()
    
