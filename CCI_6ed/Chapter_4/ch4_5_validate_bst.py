"""Validate if a binary tree is a binary search tree."""

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

def bst_test(node):
    """Validate by running a postorder DFS traversal and make
    sure that all left values are smaller than parent values and
    all right values are greater or equal to parent values.
    Returns three values: True/False, minvalue, maxvalue"""
    # NOTE: not sufficient to just check the child nodes vs their parent.
    # ALL NODES to the left of a given node must be <
    # ALL NODES to the right of a given node must be >
    # evaluate as a post-order DFS traversal where we float
    # the max and min values back up. If leftmax < node.value and
    # rightmin >= node.value, we're good.
    lmin, lmax, rmin, rmax = (None,)*4
    if node.left:
        lbst, lmin, lmax = bst_test(node.left)
        if not lbst:
            return False, None, None
    if node.right:
        rbst, rmin, rmax = bst_test(node.right)
        if not rbst:
            return False, None, None
    if lmax is not None and lmax >= node.value:
        return False, None, None
    if rmin is not None and rmin < node.value:
        return False, None, None
    return True, \
        min([x for x in [lmin, lmax, rmin, rmax, node.value] if x is not None]), \
        max([x for x in [lmin, lmax, rmin, rmax, node.value] if x is not None])
    
if __name__ == "__main__":
    value_list = [32, 16, 8, 4, 2, 1, 0, 3, 6, 5, 7, 12, 10, 9, 11, 14, 13, 15, 24, 20, 18, 17, 19, 22, 21, 23, 28, 26, 25, 27, 30, 29, 31, 48, 40, 36, 34, 33, 35, 38, 37, 39, 44, 42, 41, 43, 46, 45, 47, 56, 52, 50, 49, 51, 54, 53, 55, 60, 58, 57, 59, 62, 61, 63]
    root = BSTreeNode(None)
    for value in value_list:
        root.add(value)
    # should be a nice BST at this point
    print('BST Check: {} min: {} max: {}'.format(*bst_test(root)))
    # This will break it in a subtle way
    root.left.left.left.left.left.right = BSTreeNode(42)
    print('BST Check: {} min: {} max: {}'.format(*bst_test(root)))

    
    
    
    
    
