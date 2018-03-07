from linked_lists import ListNode

# This is the second part of the problem that says the digits
# are stored in forward order.

def l2num(head):
    value = 0
    for node in head.node_chain():
        value *= 10
        value += node.value
    print(value)
    return value

def sum_lists(first, second):
    """Given the header nodes of two linked lists, where
    digits of a number are stored in forward order,
    sum the values and return the answer as a new linked
    list in the same format."""
    value = l2num(first) + l2num(second)
    print(value)
    value = list(str(value))
    start, last = ListNode.from_list(value)
    return start

first, _  = ListNode.from_list([6,1,7])
second, _ = ListNode.from_list([2,9,5])

answer = sum_lists(first, second)
print(answer.print_chain())

