# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        fakehead = ListNode(0)
        fakehead.next = head
        while head and head.next:
            if head.next.val < head.val:
                _next = head.next
                start = fakehead
                while start.next.val < _next.val:
                    start = start.next

                head.next = _next.next
                _next.next = start.next
                start.next = _next

            else:
                head = head.next

        return fakehead.next
