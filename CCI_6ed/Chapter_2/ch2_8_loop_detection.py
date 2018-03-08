from linked_lists import ListNode

def find_loop(head):
    """Given a linked list, return the node that begins the loop."""
    seen = set()
    seen.add(head)
    current_node = head
    while current_node.next_node is not None:
        if current_node.next_node in seen:
            return current_node.next_node
        seen.add(current_node.next_node)
        current_node = current_node.next_node
    return None

if __name__ == "__main__":
    head, tail = ListNode.from_list(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    M_node = head.find('M')
    tail.next_node = M_node
    loop = find_loop(head)
    if loop is not None:
        print('Loop found at node with value: {}'.format(loop.value))
    else:
        print('No loop found.')

    
