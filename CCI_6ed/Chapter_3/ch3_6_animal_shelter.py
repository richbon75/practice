"""Keep queues of cats and dogs. Release only the oldest cat, oldest dog,
or the oldest animal of any type."""

from time import time
from collections import deque

class Animal(object):

    def __init__(self, name):
        self.name = name
        self.arrival_time = time()

class Shelter(object):
    """A shelter provides a queue for each animal type."""
    accepted_animals = {"cat", "dog"}

    def __init__(self):
        self.animals = dict()
        for animal in self.accepted_animals:
            self.animals[animal] = deque()

    def enqueue(self, animal_type, name):
        if animal_type not in self.accepted_animals:
            raise ValueError('Unsupported animal type: {}'.format(animal_type))
        self.animals[animal_type].append(Animal(name))

    def dequeue(self, animal_type = None):
        """Return the oldest animal of the desired type, or oldest of
        all animals if no type specified."""
        if animal_type in self.accepted_animals:
            return self.animals[animal_type].popleft()
        elif animal_type is None:
            oldest_type = None
            oldest_time = None
            for animal_type in self.animals:
                if self.animals[animal_type]:
                    if oldest_time is None \
                       or self.animals[animal_type][0].arrival_time < oldest_time:
                        oldest_type = animal_type
                        oldest_time = self.animals[animal_type][0].arrival_time
            if oldest_type:
                return self.dequeue(animal_type = oldest_type)
            return IndexError("No animals left in the shelter.")
        else:
            raise ValueError('Unsupported animal type: {}'.format(animal_type))
    

if __name__ == "__main__":
    shelter = Shelter()
    shelter.enqueue('cat','fluffy')
    shelter.enqueue('dog','rex')
    shelter.enqueue('cat','muffin')
    shelter.enqueue('cat','susan')
    shelter.enqueue('dog','king')
    shelter.enqueue('dog','murphy')
    
