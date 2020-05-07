# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue = [(root.val, root, 0)]
        parent, depth = None, None
        while queue:
            p, cur, d = queue.pop()
            if not cur:
                continue

            if cur.val == x or cur.val == y:
                if parent:
                    return True if d == depth and p != parent else False

                else:
                    parent = p
                    depth = d

            queue = [(cur.val, cur.left, d + 1),
                     (cur.val, cur.right, d + 1)] + queue

        return False
