# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        ans, cur, prev = None, head, None
        while cur:
            odd, even = cur, cur.next
            if odd and even:
                odd.next = even.next
                even.next = odd
                if ans is None:
                    ans = even
                if prev:
                    prev.next = even

            prev = odd
            cur = odd.next

        if ans is None and head:
            return head
        return ans
