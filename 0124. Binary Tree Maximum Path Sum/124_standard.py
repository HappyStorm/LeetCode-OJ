# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = -sys.maxsize

    def maxPathBranch(self, root: TreeNode) -> int:
        if not root:
            return 0

        left = max(0, self.maxPathBranch(root.left))
        right = max(0, self.maxPathBranch(root.right))
        self.ans = max(self.ans, left + right + root.val)

        return root.val + max(left, right)

    def maxPathSum(self, root: TreeNode) -> int:
        self.maxPathBranch(root)
        return self.ans

