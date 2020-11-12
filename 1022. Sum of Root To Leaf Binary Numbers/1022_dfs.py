# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def dfs(node, cur, _sum):
            if node:
                cur = (cur << 1) | node.val

                if node.left is None and node.right is None:
                    _sum += cur

                lsum = dfs(node.left, cur, _sum)
                rsum = dfs(node.right, cur, _sum)

                return _sum + lsum + rsum
            else:
                return 0

        return dfs(root, 0, 0)
