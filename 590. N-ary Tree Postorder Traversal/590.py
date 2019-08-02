"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []

        ans = []
        for c in root.children:
            ans += self.postorder(c)

        ans += [root.val]
        return ans