"""
Problem: Connected components, cycle detection, Kruskal's MST
Pattern: Union-Find (Disjoint Set Union)
Key Insight: Path compression in find() flattens tree, near O(1) per find
    Union by rank in union() always attach smaller tree under larger
Time Complexity: O(α(n)) ≈ O(1) per operation
Space Complexity: O(n)
"""
class UnionFind:
    def __init__(self, node_count):
        self.parent = [i for i in range(node_count)]
        self.rank = [0] * node_count
    
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, node1, node2):
        rn1, rn2 = self.find(node1), self.find(node2)
        # Commmon case: already in the same set
        if rn1 == rn2:
            return False
        if self.rank[rn1] < self.rank[rn2]:
            rn1, rn2 = rn2, rn1
        self.parent[rn2] = rn1
        if self.rank[rn1] == self.rank[rn2]:
            self.rank[rn1] += 1
        return True

def kruskals_mst(num_nodes, edges):
    edges.sort()
    uf = UnionFind(num_nodes)
    mst = []
    mst_cost = 0

    for w, u, v in edges:
        if uf.union(u, v):
            mst.append((w, u, v))
            mst_cost += w
        if len(mst) == num_nodes - 1:
            break
    return mst, mst_cost

# Test code
if __name__ == "__main__":
    uf = UnionFind(5)
    print("Root nodes for each node prior to any union operations:")
    for i in range(5):
        print("find({i}): {res}".format(i=i, res=uf.find(i)))
    print("\nPerforming union operations:")
    edges = [(0, 1), (1, 2), (2, 3), (3, 4), (0, 2)]
    for n1, n2 in edges:
       res = uf.union(n1, n2)
       print(f"Union({n1}, {n2}): {res} => Cycle detected: {not res}")

    print("\nPerforming Kruskal's MST:")
    edges_kruskal = [(1, 2, 1), (1, 3, 4), (1, 4, 3), (2, 3, 2), (3, 4, 5)]
    mst, mst_cost = kruskals_mst(6, edges_kruskal)
    print(f"Input edges: {edges_kruskal}")
    print(f"MST: {mst}")
    print(f"MST Cost: {mst_cost}")