from linked_lists import ListNode

def kth_to_last(head, k):
    """Returns the kth to last node of the list.
    The last node of the list is k=1."""
    # Runs in O(N). Runs through list once to count,
    # again to get Kth to last.
    node_count = 0
    for node in head.node_chain():
        node_count += 1
    if k > node_count:
        return None
    countdown = node_count - k
    current_node = head
    while countdown > 0:
        current_node = current_node.next_node
        countdown -= 1
    return current_node

start, last = ListNode.from_list(['A','B','C','D','E','F','G','H','I'])

print(kth_to_last(start, 3).value)
print(kth_to_last(start, 1).value)
print(kth_to_last(start, 9).value)

