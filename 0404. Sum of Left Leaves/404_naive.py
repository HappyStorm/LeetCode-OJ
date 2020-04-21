# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0

        ans = 0
        if root.left:
            ans += self.sumOfLeftLeaves(root.left)
            if not root.left.left and not root.left.right:
                ans += root.left.val

        if root.right:
            ans += self.sumOfLeftLeaves(root.right)

        return ans
