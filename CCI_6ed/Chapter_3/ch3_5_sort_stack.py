"""Sort the contents of a stack so that the smallest values are on top,
using only another stack."""

from collections import deque

class SortStack(object):

    def __init__(self, iterator):
        self.queue_a = deque()
        self.queue_b = deque()
        self.sorted = False
        for value in iterator:
            self.queue_a.append(value)

    def print(self):
        print('a : {}'.format(self.queue_a))
        # print('b : {}'.format(self.queue_b))

    def minpour(self):
        temp = self.queue_a.pop()
        while self.queue_a:
            if self.queue_a[-1] < temp:
                self.queue_b.append(self.queue_a.pop())
            else:
                self.queue_b.append(temp)
                temp = self.queue_a.pop()
        self.queue_b.append(temp)
        self.queue_a, self.queue_b = self.queue_b, self.queue_a

    def maxpour(self):
        sort_check = True
        temp = self.queue_a.pop()
        while self.queue_a:
            if self.queue_a[-1] > temp:
                if self.queue_b and self.queue_b[-1] < self.queue_a[-1]:
                    sort_check = False
                self.queue_b.append(self.queue_a.pop())
            else:
                if self.queue_b and self.queue_b[-1] < temp:
                    sort_check = False
                self.queue_b.append(temp)
                temp = self.queue_a.pop()
        if self.queue_b and self.queue_b[-1] < temp:
            sort_check = False
        self.queue_b.append(temp)
        self.queue_a, self.queue_b = self.queue_b, self.queue_a
        self.sorted = sort_check

    def sort(self):
        while not self.sorted:
            self.minpour()
            self.print()
            self.maxpour()
            self.print()

    
    
