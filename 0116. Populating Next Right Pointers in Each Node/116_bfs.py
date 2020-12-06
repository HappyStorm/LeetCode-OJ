"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return
        queue = [root]
        while queue:
            _len = len(queue)
            for i in range(_len):
                cur = queue.pop()
                cur.next = None if i == _len-1 else queue[-1]
                if cur.left:
                    queue = [cur.left] + queue
                if cur.right:
                    queue = [cur.right] + queue
        return root
