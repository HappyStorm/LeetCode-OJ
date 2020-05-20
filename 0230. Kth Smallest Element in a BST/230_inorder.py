# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        nodes = []

        ct, cur = 0, root
        while cur or nodes:
            if cur:
                nodes += [cur]
                cur = cur.left

            else:
                top = nodes.pop()
                ct += 1

                if ct == k:
                    return top.val

                else:
                    cur = top.right

        return root.val
