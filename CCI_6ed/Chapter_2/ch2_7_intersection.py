from linked_lists import ListNode

def intersection(head_a, head_b):
    """If the two lists intersect, return the first node they
    have in common."""
    # Runs in O(N) and storage O(1)
    # let's find the lengths and tails of both lists
    len_a = 1
    tail_a = head_a
    while tail_a.next_node is not None:
        len_a += 1
        tail_a = tail_a.next_node
    len_b = 1
    tail_b = head_b
    while tail_b.next_node is not None:
        len_b += 1
        tail_b = tail_b.next_node

    # if the tails are not the same, there's no intersection at all.
    if tail_a is not tail_b:
        return False

    # if one list is longer than the other, let's skip ahead in the
    # longer list.  They can't intersect before this anyway.
    diff = len_a - len_b
    while diff > 0:
        head_a = head_a.next_node
        diff -= 1
    while diff < 0:
        head_b = head_b.next_node
        diff += 1

    # for lists of the same length, any intersection will happen
    # at the same node depth of each list, so we can scan going forward
    # and stop when we have a match
    if head_a is head_b:
        return head_a
    while head_a.next_node:
        head_a = head_a.next_node
        head_b = head_b.next_node
        if head_a is head_b:
            return head_a
    return None

if __name__ == "__main__":
    head_a, tail_a = ListNode.from_list(['A','B','C','D','E','F','G','H','I'])
    head_b, tail_b = ListNode.from_list(['J','K','L','M','N'])
    common_c, _ = ListNode.from_list([1,2,3,4,5])
    tail_a.next_node = common_c
    tail_b.next_node = common_c

    result = intersection(head_a, tail_b)
    if result:
        print('Intersection found!')
        result.print_chain()
    else:
        print('No intersect found.')

