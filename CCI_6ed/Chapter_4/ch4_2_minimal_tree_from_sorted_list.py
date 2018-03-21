"""Given a sorted list, build a binary search tree with minimal height."""

from math import floor, ceil, log2

# NOTE: This runs in O(NlogN) time - we could do this in O(N) if we
# built subtrees instead of doing a full tree search for every
# insertion.

class BSTreeNode(object):
    """Basic binary search tree object"""

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def add(self, value):
        """Add a new value to the tree."""
        if self.value is None:
            self.value = value
            return
        if value < self.value:
            if self.left:
                self.left.add(value)
            else:
                self.left = __class__(value) 
        else:
            if self.right:
                self.right.add(value)
            else:
                self.right = __class__(value)                          

    def visit_inorder(self, depth=0, do_on_visit=None):
        """Print an in-order traversal of the tree, and return
        the maximum depth of the tree."""
        max_depth = depth+1
        if self.left:
            max_depth = max(self.left.visit_inorder(depth=depth+1, do_on_visit=do_on_visit), max_depth)
        if do_on_visit:
            do_on_visit(self.value)
        if self.right:
            max_depth = max(self.right.visit_inorder(depth=depth+1, do_on_visit=do_on_visit), max_depth)
        return max_depth

def min_order_iter(valuelist):
    """Visit a sorted list in a useful order for inserting
    into a minimum height binary tree."""
    if valuelist:
        midpoint = floor(len(valuelist)/2)
        yield valuelist[midpoint]
        yield from min_order_iter(valuelist[0:midpoint])
        yield from min_order_iter(valuelist[midpoint+1:])

def min_tree_from_sorted_list(valuelist):
    """To make a minimum tree from a sorted list,
    we need to add the values to the tree in the proper order,
    basically always trying to insert the middle value
    in any sublist, and recurse on the front and back halfs of the lists."""
    root = BSTreeNode()
    for value in min_order_iter(valuelist):
        root.add(value)
    return root

if __name__ == "__main__":
    sorted_list = [i for i in range(64)]
    root = min_tree_from_sorted_list(sorted_list)
    tree_depth = root.visit_inorder(do_on_visit=print)
    print('tree_depth = {}'.format(tree_depth))
    print('minimum possible depth = {}'.format(ceil(log2(len(sorted_list)+1))))
        
