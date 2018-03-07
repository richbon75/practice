
class ListNode(object):
    """A simple singly-linked node to use in some of the
    problems for this chapter."""

    def __init__(self, value = None):
        self.value = value
        self.next_node = None

    @classmethod
    def from_list(self, values = []):
        """Creates a linked list from a list of values.
        Returns (first_node, last_node)"""
        if len(values) > 1:
            first_node = __class__(values[0])
            return first_node, first_node.add_list(values[1:])
        return None, None

    def add(self, value = None):
        """Creates a new node, appends it to the current node,
        and returns that new node."""
        self.next_node = __class__(value)
        return self.next_node

    def add_list(self, values = []):
        """Given a list, iterate through them and add them to the list.
        Returns the last added node."""
        current_node = self
        for value in values:
            current_node = current_node.add(value)
        return current_node

    def delete_next(self):
        """Deletes (by dereferencing) the next node.
        Returns the current node."""
        deleted_node = self.next_node
        if deleted_node:
            self.next_node = deleted_node.next_node
            deleted_node.next_node = None
        return self

    def value_chain(self):
        """Generator that iterates through all values
        in the current node and down the list."""
        current_node = self
        while current_node:
            yield current_node.value
            current_node = current_node.next_node

    def print_chain(self):
        """Print values of all nodes from the current node"""
        print([value for value in self.value_chain()])

    def node_chain(self):
        """Generator that iterates through all nodes
        from the current node down the list."""
        current_node = self
        while current_node:
            yield current_node
            current_node = current_node.next_node

    def find(self, value, stop_node=None):
        """Iterate through the nodes and return the first node
        with a matching value. If supplied, search will
        stop at indicated stop node."""
        current_node = self
        while current_node:
            if current_node.value == value:
                return current_node
            if current_node is not stop_node:
                current_node = current_node.next_node
            else:
                return None
        return None

    def find_tail(self):
        """Starting at the current node, iterate until the last
        node is found, and return that."""
        current_node = self
        while current_node.next_node:
            current_node = current_node.next_node
        return current_node

    def delete(self, value):
        """Iterates through the nodes and deletes the first
        node with a matching value. Returns a reference to
        the first node in the remaining list. (Will be self
        unless self contained the value.)"""
        head = self
        if head.value == value:
            new_head = head.next_node
            head.next_node = None
            return new_head
        current_node = head
        if current_node.next_node:
            if current_node.next_node.value == value:
                current_node.delete_next()
                return head
            current_node = current_node.next_node
        return head

            

        

            
