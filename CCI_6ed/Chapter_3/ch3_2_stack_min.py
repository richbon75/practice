"""Design a stack which, in addition to push and pop,
has a function min() which returns the minimum element.
Push, pop and min should all operate in O(1) time."""

from collections import deque

# Approach: Keep two stacks, the primary stack and a
# smaller stack of just the min values.  If the
# current min() value is popped off the main stack,
# also pop the top value off the min_stack.
# The current min() value is just a peek of the min_stack.

class MinStack(object):
    """Stack which can tell you the current min"""

    def __init__(self):
        self.main_stack = deque()
        self.min_stack = deque()

    def __len__(self):
        return len(self.main_stack)

    def min(self):
        """Return current min value"""
        if self.min_stack:
            return self.min_stack[-1]
        return None

    def push(self, value):
        self.main_stack.append(value)
        # if it's less than or equal to the current min value
        # push it on the min stack
        if self.min() is None or value <= self.min():
                self.min_stack.append(value)

    def pop(self):
        popval = self.main_stack.pop()
        if self.min() == popval:
            self.min_stack.pop()

    def pile(self, iterable):
        """Push a bunch of values on the stack."""
        for value in iterable:
            self.push(value)

if __name__ == "__main__":
    from random import randint
    ms = MinStack()
    ms.pile([randint(0,100) for _ in range(20)])
    print(ms.main_stack)
    print(ms.min_stack)
    

