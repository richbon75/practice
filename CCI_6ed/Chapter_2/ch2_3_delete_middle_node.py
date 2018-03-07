from linked_lists import ListNode

def del_middle_node(node):
    """Removes the value of this node from the list.
    Returns a reference to the next node.
    We can't do this to the last node, because then
    we really do need to delete it, but can't update
    its parent's reference to it."""
    # We don't really delete this node, because we
    # have to preserve it's parent's reference.
    # So we actually delete the next node and move it's
    # value and pointer up to this node.
    # Runs in O(1)
    if node.next_node is None:
        raise ValueError('Cannot delete last node with this function.')
    killnode = node.next_node
    node.value = killnode.value
    node.next_node = killnode.next_node
    killnode.next_node = None
    return node

start, last = ListNode.from_list(['A','B','C','D','E','F','G','H','I'])
start.print_chain()

E_node = start.find('E')
del_middle_node(E_node)
start.print_chain()

del_middle_node(start)
start.print_chain()

# del_middle_node(last)


