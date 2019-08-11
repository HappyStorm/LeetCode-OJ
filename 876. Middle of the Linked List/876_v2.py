# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        _len, cur = 0, head
        while cur:
            _len += 1
            cur = cur.next

        dis = _len - (_len // 2) - 1 if _len % 2 else _len - (_len // 2)
        while dis > 0:
            dis -= 1
            head = head.next

        return head
