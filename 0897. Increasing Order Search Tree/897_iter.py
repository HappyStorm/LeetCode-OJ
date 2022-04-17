# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        stk = []
        ans = tmp = TreeNode(None)
        cur = root
        while cur or stk:
            if cur:
                stk.append(cur)
                cur = cur.left
            else:
                node = stk.pop()
                tmp.right = TreeNode(val=node.val)
                tmp = tmp.right
                if node.right:
                    stk.append(node.right)
                    cur = node.right.left

        return ans.right
