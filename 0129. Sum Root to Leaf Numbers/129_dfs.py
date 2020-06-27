# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(cur, digits):
            if not cur:
                return 0

            digits += str(cur.val)
            left = dfs(cur.left, digits)
            right = dfs(cur.right, digits)
            return int(digits) if left == right == 0 else left + right

        return dfs(root, '')
