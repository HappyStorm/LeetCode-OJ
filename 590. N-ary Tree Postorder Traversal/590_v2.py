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

        queue, ans = [root], []
        while queue:
            cur = queue.pop(0)
            if cur is not None:
                queue = cur.children[::-1] + queue

            ans = [cur.val] + ans

        return ans