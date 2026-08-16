# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        curr = head

        while curr:
            values.append(curr.val)
            curr = curr.next
        
        values.sort()
        curr = head

        for val in values:
            curr.val = val
            curr = curr.next

        return head