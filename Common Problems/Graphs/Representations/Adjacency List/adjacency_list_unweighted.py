class Graph:
    def __init__(self):
        self.adjacent_list = {}
        self.reversed_list = {}  # Tracks incoming connections: { destination: {sources} }

    def add_vertex(self, v) -> bool:
        if v in self.adjacent_list:
            return False
        
        self.adjacent_list[v] = set()
        self.reversed_list[v] = set()
        return True

    def add_edge(self, u, v, bidirectional=False) -> bool:
        if u not in self.adjacent_list:
            self.add_vertex(u)
        if v not in self.adjacent_list:
            self.add_vertex(v)

        # Register forward connection
        self.adjacent_list[u].add(v)
        # Register incoming reverse connection
        self.reversed_list[v].add(u)

        if bidirectional:
            self.adjacent_list[v].add(u)
            self.reversed_list[u].add(v)
        return True

    def remove_edge(self, u, v, bidirectional=False) -> bool:
        if u not in self.adjacent_list or v not in self.adjacent_list:
            return False
        
        self.adjacent_list[u].discard(v)
        self.reversed_list[v].discard(u)

        if bidirectional:
            self.adjacent_list[v].discard(u)
            self.reversed_list[u].discard(v)
        return True

    def remove_vertex(self, vertex) -> bool:
        """
        Purges a vertex completely.
        Time Complexity: O(Out-Degree(V) + In-Degree(V)) instead of O(V) full-scan!
        """
        if vertex not in self.adjacent_list:
            return False
        
        # Step 1: Find all neighbors that 'vertex' points to, and remove 
        # 'vertex' from their incoming tracking maps.
        for neighbor in self.adjacent_list[vertex]:
            self.reversed_list[neighbor].discard(vertex)

        # Step 2: Find all neighbors that point TO 'vertex', and remove
        # 'vertex' from their outgoing edge sets.
        for neighbor in self.reversed_list[vertex]:
            self.adjacent_list[neighbor].discard(vertex)
        
        # Step 3: Delete the core tracking registries for this node
        del self.adjacent_list[vertex]
        del self.reversed_list[vertex]
        return True
    
    def display(self) -> dict:
        return {key: set(val) for key, val in self.adjacent_list.items()}

g = Graph()
g.add_vertex("a")
g.add_vertex("b")
g.add_vertex("c")
g.add_vertex("d")
g.add_edge("a","b")
g.add_edge("a","c")
g.add_edge("d","a")
print(g.display())
g.remove_vertex("a")
print("--Removed vertex a---")
print(g.display())