from typing import List
from collections import defaultdict


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Base cases
        if n <= 1:
            return [0]
        # Quick check for possibly invalid input (e.g. incomplete graph)
        if len(edges) < n - 1:
            return []
        
        # Build an undirected graph
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        # Initialize leaves (nodes having only one connection)
        leaves = []
        for i in range(n):
            if len(graph[i]) == 1:
                leaves.append(i)

        # Trim leaves until fewer than 3 nodes remain
        while n > 2:
            n -= len(leaves)
            new_leaves = []

            for leaf in leaves:
                # Remove the leaf and update its neighbor
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                # If the neighbor is now a leaf, add it
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves

        return leaves
