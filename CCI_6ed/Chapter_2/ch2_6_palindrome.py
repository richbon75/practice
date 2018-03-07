# Check if a linked list is a palindrome
# Recursion works in O(N) time with O(N) storage (call stack)

from linked_lists import ListNode

def is_palindrome(head):
    _, compare_result = bidirectional_compare(head, head)
    return compare_result

def reverse_visit(head):
    # Logic demo of reverse visit using recursion
    if head.next_node:
        reverse_visit(head.next_node)
    print(head.value)

def bidirectional_visit(local_head, head):
    # Logic demo of bidirectional visits using recursion
    if local_head.next_node:
        forward_visit = bidirectional_visit(local_head.next_node, head)
    else:
        forward_visit = head
    print('Reversed: {}  Forward: {}'.format(local_head.value, forward_visit.value))
    return forward_visit.next_node

def bidirectional_compare(local_head, head):
    # Returns 2 values:
    #  the forward_visit.next_node
    #  and the comparison result
    if local_head.next_node:
        forward_visit, downstream_result = bidirectional_compare(local_head.next_node, head)
    else:
        forward_visit = head
        downstream_result = True
    compare_result = downstream_result and bool(local_head.value == forward_visit.value)
    return forward_visit.next_node, compare_result

start, _  = ListNode.from_list(list("MRMOJORISIN"))
start.print_chain()
print('Is palindrome: {}'.format(is_palindrome(start)))

start, _  = ListNode.from_list(list("NAOMISEXATNOONTAXESIMOAN"))
start.print_chain()
print('Is palindrome: {}'.format(is_palindrome(start)))

start, _  = ListNode.from_list(list("A"))
start.print_chain()
print('Is palindrome: {}'.format(is_palindrome(start)))

start, _  = ListNode.from_list(list("NOTAPALINDROMETON"))
start.print_chain()
print('Is palindrome: {}'.format(is_palindrome(start)))
