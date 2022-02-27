# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 1
        queue = [(root, 0)]
        while queue:
            ln, rn = queue[0], queue[-1]
            ans = max(ans, rn[1]-ln[1]+1)

            nd_queue = []
            for node, idx in queue:
                if node.left: nd_queue.append((node.left, 2*idx))
                if node.right: nd_queue.append((node.right, 2*idx+1))
            queue = nd_queue
        return ans
