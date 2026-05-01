# Pattern: Union-Find (Disjoint Set Union)
# Use cases: connected components, cycle detection, Kruskal's MST
# Optimizations:
#   - Path compression in find()  → flattens tree, near O(1) per find
#   - Union by rank in union()    → always attach smaller tree under larger
# Time: O(α(n)) ≈ O(1) per operation | Space: O(n)
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