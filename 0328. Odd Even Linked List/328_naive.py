# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def printList(self, head: ListNode) -> ListNode:
        vals = []
        while head:
            vals += [head.val]
            head = head.next

        print("->".join(map(lambda x: str(x), vals)))

    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        odd, odd_ed, even, even_st = head, head, head.next, head.next
        while odd and even and even.next:
            odd.next = even.next if even else even
            even.next = odd.next.next if odd.next else odd
            odd = odd.next
            odd.next = even
            even = even.next

        odd.next = even_st
        return head
