"""T1 and T2 are two very large binary trees, with T1 much bigger than T2.
Create an algorithm to determine if T2 is a subtree of T1.
A tree T2 is a subtree of T1 if there exists a node n in T1 such that the
subtree of n is identical to T2. That is, if you cut off the tree
at node n, the two trees would be identical."""

from random import random, randint

class BinaryTreeNode(object):
    """Binary tree node - NOT A SEARCH TREE"""

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def add(self, value):
        """Add a new value to the tree. If the target node
        is full, find a new spot at random."""
        if self.value is None:
            self.value = value
        if random() > 0.5:
            if self.left:
                self.left.add(value)
            else:
                self.left = __class__(value)
        else:
            if self.right:
                self.right.add(value)
            else:
                self.right = __class__(value)

def compare_trees(tree1, tree2):
    """Compares two trees and decides if they're the same.
    Must have identical structure and values."""
    if tree1.value != tree2.value:
        return False
    if (bool(tree1.left) != bool(tree2.left) or
        bool(tree1.right) != bool(tree2.right)):
        return False
    if tree1.left and not compare_trees(tree1.left, tree2.left):
        return False
    if tree1.right and not compare_trees(tree1.right, tree2.right):
        return False
    return True

def is_subtree(T1, T2):
    """Determines if T2 is a subtree of T1"""
    # Preorder DFS search and test each node where the value = T2's root value
    if T1.value == T2.value and compare_trees(T1, T2):
        return True
    if T1.left and is_subtree(T1.left, T2):
        return True
    if T1.right and is_subtree(T1.right, T2):
        return True
    return False    

if __name__ == "__main__":
    # Build up two random trees
    T2 = BinaryTreeNode()
    for _ in range(10):
        T2.add(randint(0,100))
    T1 = BinaryTreeNode()
    for _ in range(10000):
        T1.add(randint(0,100))
    # Barring amazing coincidence, these will not match
    print(is_subtree(T1, T2))
    # Stash T2 as a subtree in T1 (we won't compare the actual objects,
    # just the values and structures)
    T1.left.left.right.right.left.right.right = T2
    # Now we should see a match
    print(is_subtree(T1, T2))

    

    
        
        
