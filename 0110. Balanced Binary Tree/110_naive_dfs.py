# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def postorder(node, depth):
            if not node:
                return depth
            lh = postorder(node.left, depth+1)
            rh = postorder(node.right, depth+1)
            if abs(lh-rh) > 1:
                return -1

            return max(lh, rh)

        return True if postorder(root, 1) > 0 else False
