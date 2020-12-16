# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.cur = None

        def inorder(node):
            if not node:
                return True
            left = inorder(node.left)
            if self.cur is not None and self.cur >= node.val:
                return False
            self.cur = node.val
            right = inorder(node.right)
            return left and right
        return inorder(root)
