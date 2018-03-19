"""Check if a binary tree is balanced.  "For the purposes of this question,
a balanced tree is defined to be a tree such that the heights of the two
subtrees of any node ever differs by more than one." """

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

def is_balanced_check(node, depth=0):
    """Returns two values - the total height of the tree
    below the node, and a boolean value indicating if all
    subtrees are balanced."""
    if not node:
        return depth, True
    leftdepth,  leftbalanced  = is_balanced_check(node.left, depth+1)
    rightdepth, rightbalanced = is_balanced_check(node.right, depth+1)
    if abs(leftdepth-rightdepth) > 1:
        balanced = False
    else:
        balanced = leftbalanced and rightbalanced
    depth = max(leftdepth, rightdepth)
    return depth, balanced

def is_balanced(node):
    """Determine if the binary tree beneath this node is balanced."""
    depth, balanced = is_balanced_check(node)
    return balanced

if __name__ == "__main__":
    root = BSTreeNode(5)
    root.add(3)
    root.add(1)
    root.add(4)
    root.add(7)
    root.add(6)
    root.add(8)
    # Tree is complete and blanced at this point
    print(is_balanced(root))
    # Right side is only 1 node deeper, still "balanced"
    root.add(9)
    print(is_balanced(root))
    # Right side is 2 nodes deeper.  Not balanced.
    root.add(10)
    print(is_balanced(root))
    
