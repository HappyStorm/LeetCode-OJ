# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        ans = 0
        queue = [root]
        while queue:
            cur = queue.pop()
            if cur:
                ans += 1
                queue = [cur.left, cur.right] + queue

        return ans
