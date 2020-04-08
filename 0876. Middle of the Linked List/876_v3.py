# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head.next:
            return head

        cur, _len = head.next, 1
        while cur:
            cur = cur.next
            _len += 1

        cur, pt, ans_id = head.next, 1, _len//2
        while pt != ans_id:
            cur = cur.next
            pt += 1

        return cur


