"""Given a directed graph, design an algorithm to find out
whether there is a route betweent two nodes."""

from collections import deque

class Graph(object):
    """A directed graph class."""

    def __init__(self):
        """Stores a directed graph as a dictionary of sets."""
        self.edges = dict()

    def add(self, start, end):
        """Add an edge to the graph. Supply the names of the
        start node and the end node."""
        if start not in self.edges:
            self.edges[start] = set()
        self.edges[start].add(end)

    def print(self):
        """Print a representation of the Graph for testing."""
        for start in sorted(self.edges):
            print('{} : {}'.format(start, sorted(self.edges[start])))

    def is_route(self, start, end):
        """Determine if there is a route from the start node
        to the end node.  This is enough to answer the problem."""
        if start not in self.edges:
            return False
        visited = set()
        to_visit = deque()
        to_visit.append(start)
        while to_visit:
            visit_node = to_visit.popleft()
            if visit_node in visited:
                continue
            # print('Visiting {}'.format(visit_node))
            if visit_node == end:
                return True
            visited.add(visit_node)
            if visit_node in self.edges:
                to_visit.extend(self.edges[visit_node])
        return False

    def find_path_parent(self, start, end):
        """If the end node is reachable, it returns
        the parent of the end node as found in the path.
        Uses breadth-first so we always find the shortest path."""
        if start not in self.edges:
            return None
        visited = set()
        from_visit = deque()
        to_visit = deque()
        from_visit.append(start)
        to_visit.append(start)
        while to_visit:
            visit_node = to_visit.popleft()
            from_node = from_visit.popleft()
            if visit_node in visited:
                continue
            # print('Visiting from {} to {}'.format(from_node, visit_node))
            if visit_node == end:
                return from_node
            visited.add(visit_node)
            if visit_node in self.edges:
                for to_visit_node in self.edges[visit_node]:
                    from_visit.append(visit_node)
                    to_visit.append(to_visit_node)
        return None

    def find_path(self, start, end):
        """Keep building up the path from the end"""
        parent = self.find_path_parent(start,end)
        if not parent:
            return None
        path = deque([end])
        while parent and parent != start:
            path.appendleft(parent)
            parent = self.find_path_parent(start, parent)
        path.appendleft(parent)
        return path
    
def randchar(start, end):
    """Pick a random character between the two provided chars"""
    from random import randint
    return chr(randint(ord(start),ord(end)))

def test(nodes=50):
    """Generate a random graph and test for a path from
    node 'A' to 'Z'"""
    g = Graph()
    for _ in range(nodes):
        g.add(randchar('A','z'), randchar('A','z'))
    g.print()
    print("Path from A->Z: {}".format(g.find_path('A','z')))

if __name__ == "__main__":
    test(30)
          

    
