# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True

        ans, queue = True, [root]
        while queue:
            cur = queue.pop(0)
            if cur:
                if cur.val != root.val:
                    return False

                queue += [cur.left, cur.right]

        return True