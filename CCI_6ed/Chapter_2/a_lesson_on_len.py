import time

times_len_called = 0

class ListNode(object):
    """A simple singly-linked-list node to use in some practice problems."""

    def __init__(self, value = None):
        """Create a single node with the provided value."""
        self.value = value
        self.next_node = None

    def __len__(self):
        """Iterate through the nodes and return the count of
        nodes in the list."""
        # https://stackoverflow.com/questions/25291590/why-is-len-called-implicitly-on-a-custom-iterator
        # "if self.next_node" implicitly uses the len() function to test
        # for an empty container, which will result in lots of
        # crazy exponentially nested calls taking a ton of time.
        # Using "if self.next_node is not None" avoids that, and
        # allows calls to len() to complete in simple O(N) time.
        global times_len_called
        times_len_called += 1
        length = 1
        # remove "is not None" in the next line to see hideous performance  
        if self.next_node is not None:
            length += len(self.next_node)
        return length

    @classmethod
    def from_list(self, values = None):
        """Creates a linked list from a list of values.
        Returns (head, tail)"""
        if len(values) >= 1:
            head = __class__(values[0])
            tail = head
            for value in values[1:]:
                tail = tail.add(value)
            return head, tail
        return None, None

    def add(self, value = None):
        """Creates a new node, appends it to the current node,
        and returns that new node."""
        self.next_node = __class__(value)
        return self.next_node

if __name__ == "__main__":
    head, tail = ListNode.from_list(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    # Let's time how long it takes to print out the linked list.
    start_time = time.time()
    current_node = head
    # remove "is not None" in the next line to see hideous performance
    while current_node is not None:
        print(current_node.value)
        current_node = current_node.next_node
    print('Time to print: {}'.format(time.time()-start_time))
    print(f'Times len called: {times_len_called}')

        

            
