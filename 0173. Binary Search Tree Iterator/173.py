# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = self.cur = TreeNode(None)
        self.inorder(root)

    def next(self) -> int:
        self.root = self.root.right
        return self.root.val

    def hasNext(self) -> bool:
        return True if self.root and self.root.right else False

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            node.left = None
            self.cur.right = node
            self.cur = node
            self.inorder(node.right)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
