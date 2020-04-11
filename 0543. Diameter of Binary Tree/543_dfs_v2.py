# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node):
            return max(dfs(node.left), dfs(node.right)) + 1 if node else 0

        return max(dfs(root.left) + dfs(root.right),
                   max(self.diameterOfBinaryTree(root.left),
                       self.diameterOfBinaryTree(root.right))) if root else 0
