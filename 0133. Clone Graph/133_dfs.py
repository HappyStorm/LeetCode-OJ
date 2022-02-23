"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}

        def clone(node, visited):
            if not node:
                return None
            if visited.get(node):
                return visited[node]
            root = Node(val=node.val)
            visited[node] = root
            for n in node.neighbors:
                root.neighbors.append(clone(n, visited))
            return root

        return clone(node, visited)
