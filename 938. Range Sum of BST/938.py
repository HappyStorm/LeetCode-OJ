# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root is None:
            return 0

        ans = 0
        if L > root.val:
            ans += self.rangeSumBST(root.right, L, R)

        elif R < root.val:
            ans += self.rangeSumBST(root.left, L, R)

        else:
            ans += root.val
            ans += self.rangeSumBST(root.right, L, R)
            ans += self.rangeSumBST(root.left, L, R)

        return ans

        return