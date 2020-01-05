"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        max_d = 0
        for c in root.children:
            max_d = max(max_d, self.maxDepth(c))

        return max_d + 1
