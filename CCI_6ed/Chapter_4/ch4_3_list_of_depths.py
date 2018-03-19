
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

def make_level_dictionary(node, levels = None, depth = 0):
    """Version of answer that builds up a dictionary of level lists."""
    if levels is None:
        levels = dict()
    # basically, DFS inorder traversal adding values to the dictionary
    if node.left:
        make_level_dictionary(node.left, levels = levels, depth = depth+1)
    if depth not in levels:
        levels[depth] = list()
    levels[depth].append(node.value)
    if node.right:
        make_level_dictionary(node.right, levels = levels, depth = depth+1)
    return levels

def make_level_list(node, levels = None, depth = 0):
    """Version of answer that builds up a list of level lists."""
    if levels is None:
        levels = list()
    # DFS preorder traversal adding values to the list
    # (*preorder* so we are sure we encounter each new level in numerical order
    # to simplify creating new levels in the list)
    if len(levels) < depth+1:
        levels.append(list())
    levels[depth].append(node.value)
    if node.left:
        make_level_list(node.left, levels = levels, depth = depth+1)
    if node.right:
        make_level_list(node.right, levels = levels, depth = depth+1)
    return levels

if __name__ == "__main__":
    value_list = [32, 16, 8, 4, 2, 1, 0, 3, 6, 5, 7, 12, 10, 9, 11, 14, 13, 15, 24, 20, 18, 17, 19, 22, 21, 23, 28, 26, 25, 27, 30, 29, 31, 48, 40, 36, 34, 33, 35, 38, 37, 39, 44, 42, 41, 43, 46, 45, 47, 56, 52, 50, 49, 51, 54, 53, 55, 60, 58, 57, 59, 62, 61, 63]
    root = BSTreeNode(None)
    for value in value_list:
        root.add(value)
    level_dict = make_level_dictionary(root)
    print(level_dict)
    level_list = make_level_list(root)
    print(level_list)

    

