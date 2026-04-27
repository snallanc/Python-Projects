from collections import defaultdict
from collections import deque

class Graph:
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed
        self.num_edges = 0

    def add_edge(self, v, adj_v):
        if adj_v in self.graph[v]:
            return
        self.graph[v].append(adj_v)
        self.num_edges += 1
        if self.directed or v in self.graph[adj_v]:
            return
        self.graph[adj_v].append(v)
        self.num_edges += 1

    def print_graph(self):
        if not self.num_edges:
            print("Graph is empty.")
            return
        for v, adj_v in self.graph.items():
            print("Vertex {} -> Adj {}".format(v, adj_v))

    def del_edge(self, v, adj_v):
        if adj_v not in self.graph[v]:
            return
        self.graph[v].remove(adj_v)
        self.num_edges -= 1
        if self.directed or v not in self.graph[adj_v]:
            return
        self.graph[adj_v].remove(v)
        self.num_edges -= 1

    def _bfs(self, start_v, visited=None):
        if visited is None:
            visited = set()
        que = deque([start_v])
        while que:
            node = que.popleft()
            if node in visited:
                continue
            print("Visiting Node {}".format(node))
            visited.add(node)
            for n in self.graph[node]:
                if n in visited:
                    continue
                que.append(n)
    
    def _dfs(self, start_v, visited=None):
        if visited is None:
            visited = set()
        print("Visiting Node {}".format(start_v))
        visited.add(start_v)
        for n in self.graph[start_v]:
            if n in visited:
                continue
            self._dfs(n, visited)
    
    def bfs(self):
        visited = set()
        for v in self.graph:
            if v in visited:
                continue
            self._bfs(v, visited)
    
    def dfs(self):
        visited = set()
        for v in self.graph:
            if v in visited:
                continue
            self._dfs(v, visited)

# Test code
if __name__ == "__main__":
    graph = Graph(directed=False)
    edges = [(1, 2), (1, 3), (3, 4), (2, 4), (1, 5), (3, 5)]
    for edge in edges:
        graph.add_edge(*edge)
    print("Graph after adding edges: #Edges = {}".format(graph.num_edges))
    graph.print_graph()

    print("\nPerforming BFS traversal:")
    graph.bfs()
    print("\nPerforming DFS traversal:")
    graph.dfs()

    for edge in edges:
        graph.del_edge(*edge)
        print("\nGraph after deleting edge {}: #Edges = {}".format(edge, graph.num_edges))
        graph.print_graph()