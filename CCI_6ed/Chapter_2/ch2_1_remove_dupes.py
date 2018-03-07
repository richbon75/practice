from linked_lists import ListNode

def remove_dupes(head):
    """Given a reference to the start of a list,
    remove any duplicate values."""
    # Runs in O(N) - Makes a single pass through the list
    # and lookups to seen take O(1) time each.
    seen = set()
    current_node = head
    seen.add(current_node.value)
    while current_node.next_node:
        if current_node.next_node.value in seen:
            current_node.delete_next()
            continue
        seen.add(current_node.next_node.value)
        current_node = current_node.next_node
    return head

def remove_dupes_notemp(head):
    """Removes duplicate values from the unsorted list
    but does NOT require extra storage for duplicate values.
    Returns pointer to the head of the list."""
    # Runs in O(N^2)
    current_node = head
    while current_node.next_node:
        if head.find(current_node.next_node.value, current_node):
            current_node.delete_next()
        else:
            current_node = current_node.next_node
    return head

start, last = ListNode.from_list(['A','B','C','D','B','C','E','F','A'])

start.print_chain()
remove_dupes(start)
start.print_chain()
print ('=' * 25)

start, last = ListNode.from_list(['A','B','C','D','B','C','E','F','A'])
start.print_chain()
remove_dupes(start)
start.print_chain()



