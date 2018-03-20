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

def bst_test(node, left_ancestor = None, right_ancestor = None):
    """Validates DFS in a more efficient way, does preorder DFS
    and checks each node against their last "ancestor from the left"
    and their last "ancestor from the right". This way we don't
    have to bubble up anything except the True/False results."""
    if left_ancestor is not None and node.value < left_ancestor:
        return False
    if right_ancestor is not None and node.value >= right_ancestor:
        return False
    is_bst = True
    if node.left:
        is_bst &= bst_test(node.left, left_ancestor, node.value)
    if not is_bst:
        return False
    if node.right:
        is_bst &= bst_test(node.right, node.value, right_ancestor)
    return is_bst

    
if __name__ == "__main__":
    value_list = [32, 16, 8, 4, 2, 1, 0, 3, 6, 5, 7, 12, 10, 9, 11, 14, 13, 15, 24, 20, 18, 17, 19, 22, 21, 23, 28, 26, 25, 27, 30, 29, 31, 48, 40, 36, 34, 33, 35, 38, 37, 39, 44, 42, 41, 43, 46, 45, 47, 56, 52, 50, 49, 51, 54, 53, 55, 60, 58, 57, 59, 62, 61, 63]
    root = BSTreeNode(None)
    for value in value_list:
        root.add(value)
    # should be a nice BST at this point
    print('BST Check Better: {}'.format(bst_test(root)))
    # This will break it in a subtle way
    root.left.right.value = 22.5
    print('BST Check Better: {}'.format(bst_test(root)))

    
    
    
    
