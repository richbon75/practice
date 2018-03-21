"""Write a procedure that, given one node of a BST, finds the NEXT node
in an in-order search. Assume nodes have links to their parents."""

class BSTreeNode(object):
    """Basic binary search tree object - WITH PARENT LINK"""

    def __init__(self, value=None, parent=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent

    def add(self, value, parent=None):
        """Add a new value to the tree."""
        if self.value is None:
            self.value = value
            self.parent = parent
            return
        if value < self.value:
            if self.left:
                self.left.add(value, parent=self)
            else:
                self.left = __class__(value, parent=self) 
        else:
            if self.right:
                self.right.add(value, parent=self)
            else:
                self.right = __class__(value, parent=self)

def find_successor(node):
    """Find the "next" node to visit."""
    # If right child exists, find right child's left-most descendant.
    if node.right is not None:
        node = node.right
        while node.left is not None:
            node = node.left
        return node
    # If no right child, continue up the tree until we are coming
    # from a node's left child, then visit that node.
    last_node = node.right
    while last_node is node.right:
        if node.parent is None:
            return None
        last_node, node = node, node.parent
    # if we get here, we've come up from a left child
    return node

if __name__ == "__main__":
    value_list = [32, 16, 8, 4, 2, 1, 0, 3, 6, 5, 7, 12, 10, 9, 11, 14, 13, 15, 24, 20, 18, 17, 19, 22, 21, 23, 28, 26, 25, 27, 30, 29, 31, 48, 40, 36, 34, 33, 35, 38, 37, 39, 44, 42, 41, 43, 46, 45, 47, 56, 52, 50, 49, 51, 54, 53, 55, 60, 58, 57, 59, 62, 61, 63]
    root = BSTreeNode(None)
    for value in value_list:
        root.add(value)
    print(find_successor(root).value)
    
