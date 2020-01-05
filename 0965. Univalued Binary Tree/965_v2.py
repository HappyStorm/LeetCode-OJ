# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        left = (not root.left or root.left.val == root.val
                and self.isUnivalTree(root.left))
        right = (not root.right or root.right.val == root.val
                 and self.isUnivalTree(root.right))

        return left and right
