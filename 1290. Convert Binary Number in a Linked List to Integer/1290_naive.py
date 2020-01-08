# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        vals = []
        while head:
            vals += [head.val]
            head = head.next

        vals = [(2**i) * v  for i, v in enumerate(vals[::-1])]
        return sum(vals)