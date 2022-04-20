# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.nodes, self.ct = [], -1

        stk = []
        cur = root
        while cur or stk:
            if cur:
                stk.append(cur)
                cur = cur.left
            else:
                _node = stk.pop()
                self.nodes.append(_node)
                if _node.right:
                    stk.append(_node.right)
                    cur = _node.right.left

    def next(self) -> int:
        self.ct += 1
        return self.nodes[self.ct].val

    def hasNext(self) -> bool:
        if self.ct + 1 >= len(self.nodes):
            return False
        else:
            return True


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
