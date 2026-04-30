import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../ds_custom'))
from heap import MinHeap
from graph import Graph
from collections import defaultdict

def get_path(sp_adj, target):
    path = []
    while target:
        path.append(target)
        target = sp_adj[target][1]
    return path[::-1]

def dijkstra_shortest_path(graph, source_v):
    visited = set()
    mh = MinHeap([(0, source_v)])
    sp_adj = defaultdict(lambda: (float('inf'), None))
    sp_adj[source_v] = (0, None)
    while mh:
        dist, v = mh.pop()              # unpack (distance, node)
        if v in visited:
            continue
        visited.add(v)
        for n, w in graph.graph[v]:
            if n in visited:
                continue
            new_dist = dist + w
            if new_dist < sp_adj[n][0]:
                sp_adj[n] = (new_dist, v)
                mh.push((new_dist, n))  # push (new_distance, neighbor)
    return sp_adj

if __name__ == "__main__":
    g = Graph()
    g.add_edge(1, 2, 4)
    g.add_edge(1, 3, 1)
    g.add_edge(3, 2, 2)
    g.add_edge(2, 4, 1)
    g.add_edge(3, 4, 5)
    sp_adj = dijkstra_shortest_path(g, 1)
    print("Shortest path adjacency list:")
    for v in sp_adj:
        print(f"\tNode {v}: Distance = {sp_adj[v][0]}, Previous Node = {sp_adj[v][1]}")
    for target in range(1, 5):
        path = get_path(sp_adj, target)
        print("Shortest path to {}: {}".format(target, path))