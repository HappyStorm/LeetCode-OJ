# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.ans = 0
        counter = {i: 0 for i in range(1, 10)}

        def dfs(node, counter):
            if not node.left and not node.right:
                any_odd = False
                for d in counter.values():
                    odd_val = d % 2
                    if odd_val and any_odd:
                        return
                    if odd_val and not any_odd:
                        any_odd = True
                self.ans += 1
                return
            else:
                if node.left:
                    counter[node.left.val] += 1
                    dfs(node.left, counter)
                    counter[node.left.val] -= 1
                if node.right:
                    counter[node.right.val] += 1
                    dfs(node.right, counter)
                    counter[node.right.val] -= 1
        counter[root.val] += 1
        dfs(root, counter)
        return self.ans
