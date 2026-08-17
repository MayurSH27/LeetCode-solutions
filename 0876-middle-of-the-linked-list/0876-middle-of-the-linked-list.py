# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        len = 0

        while curr:
            len += 1
            curr = curr.next

        len = len//2 + 1
        count = 0

        while head:
            count += 1
            if count is len:
                return head
            head = head.next