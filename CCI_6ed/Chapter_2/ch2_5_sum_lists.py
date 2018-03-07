from linked_lists import ListNode

# runs in O(N) time
# each input list traversed once
# output list reversed and traversed (O(2N))

def l2num_reverse(head):
    value = 0
    place = 1
    for node in head.node_chain():
        value += node.value * place
        place *= 10
    return value

def sum_lists(first, second):
    """Given the header nodes of two linked lists, where
    digits of a number are stored in reverse order,
    sum the values and return the answer as a new linked
    list in the same format."""
    value = l2num_reverse(first) + l2num_reverse(second)
    value = list(str(value))
    value.reverse()
    start, last = ListNode.from_list(value)
    return start

first, _  = ListNode.from_list([7,1,6])
second, _ = ListNode.from_list([5,9,2])

answer = sum_lists(first, second)
print(answer.print_chain())
