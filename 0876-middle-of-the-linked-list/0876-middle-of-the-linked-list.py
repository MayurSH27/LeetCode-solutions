# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        orig_head = head
        length = 0

        while head:
            length += 1
            head = head.next

        middle = length//2 + 1
        head = orig_head
        count = 0

        while head:
            count += 1
            if count == middle:
                return head
            head = head.next