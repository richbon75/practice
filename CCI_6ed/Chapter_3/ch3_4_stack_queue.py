"""Implement a queue using only two stacks."""

from collections import deque

class StackQueue(object):
    """Implements a queue using two stacks."""

    def __init__(self):
        self.in_stack = deque()
        self.out_stack = deque()

    def __len__(self):
        return len(self.in_stack) + len(self.out_stack)

    def push(self, value):
        self.in_stack.append(value)

    def dequeue(self):
        if not self.out_stack:
            self.dump_in_to_out()
        return self.out_stack.pop()

    def dump_in_to_out(self):
        """Take everything in the in_stack and dump it into the out_stack."""
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())

    def peek(self):
        if not self.out_stack:
            self.dump_in_to_out()
        return self.out_stack[-1]

    def pour(self, iterable):
        for value in iterable:
            self.push(value)
    
    
    

    
