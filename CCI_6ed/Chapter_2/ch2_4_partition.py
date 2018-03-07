from linked_lists import ListNode

def insert_node(parent, target):
    """Appends the target node to be the child of the parent
    node. If the parent already has a node, it becomes the child
    of the target."""
    target.next_node = parent.next_node
    parent.next_node = target

def partition_list(head, value):
    """Given a list and a partition value, organize the
    list so that all values < partition value are before it
    and all values > partition value come after it.
    Returns the head and tail of the list."""
    # according to a closer read of the problem, nodes with
    # the partition value need not be between the sections.
    # They can be anywhere in the right-side.
    # This function's answers are still valid answers to
    # the problem, though.
    
    newhead = None
    newmid = None
    newtail = None
    current_node = head
    while current_node:
        next_node = current_node.next_node
        if current_node.value < value:
            if not newhead:
                newhead = current_node
                newhead.next_node = None
            else:
                insert_node(newhead, current_node)
        elif current_node.value > value:
            if not newtail:
                newtail = current_node
                newtail.next_node = None
            else:
                insert_node(newtail, current_node)
        else:
            if not newmid:
                newmid = current_node
                newmid.next_node = None
            else:
                insert_node(newmid, current_node)
        current_node = next_node
    # tie all three lists together
    return_head = newhead
    if newmid:
        if return_head:
            return_head.find_tail().next_node = newmid
        else:
            return_head = newmid
    if newtail:
        if return_head:
            return_head.find_tail().next_node = newtail
        else:
            return_head = newtail
    if return_head:
        return return_head, return_head.find_tail()
    else:
        return return_head, None

start, last = ListNode.from_list([8,6,7,5,3,0,9])
start.print_chain()

start, last = partition_list(start, 4)
start.print_chain()



    
    
