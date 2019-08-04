# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0

        ans, queue = 0, [root]
        while queue:
            cur = queue.pop(0)

            if cur:
                if L > cur.val:
                    queue += [cur.right]

                elif R < cur.val:
                    queue += [cur.left]

                else:
                    ans += cur.val
                    queue += [cur.left, cur.right]

        return ans
