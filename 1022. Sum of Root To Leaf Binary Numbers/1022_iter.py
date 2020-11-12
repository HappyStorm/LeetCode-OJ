# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        ans = 0
        stack = [(root, 0)]
        while stack:
            node, _sum = stack.pop()
            if node:
                _sum = (_sum << 1) | node.val
                if node.left is None and node.right is None:
                    ans += _sum
                else:
                    stack.append((node.right, _sum))
                    stack.append((node.left, _sum))
        return ans
