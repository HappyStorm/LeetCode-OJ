# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(node):
            if not node:
                return 0

            L = dfs(node.left)
            R = dfs(node.right)
            self.ans = max(self.ans, L+R)
            return max(L+1, R+1)

        dfs(root)
        return self.ans
