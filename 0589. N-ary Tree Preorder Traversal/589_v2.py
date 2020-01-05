"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        queue, ans = [root], []

        while queue:
            cur = queue.pop(0)
            if cur is not None:
                ans += [cur.val]
                queue = cur.children + queue

        return ans
