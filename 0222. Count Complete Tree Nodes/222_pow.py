# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        ld, rd = self.get_depth(root.left), self.get_depth(root.right)
        if ld == rd:
            return 2 ** ld + self.countNodes(root.right)

        else:
            return 2 ** rd + self.countNodes(root.left)

    def get_depth(self, node):
        return 1 + self.get_depth(node.left) if node else 0
