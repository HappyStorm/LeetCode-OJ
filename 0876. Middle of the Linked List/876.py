# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        node_list = [head]
        while head.next:
            head = head.next
            node_list += [head]

        return node_list[len(node_list)//2] if len(node_list) % 2 else\
               node_list[len(node_list)//2]
