# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = head
        ans = []

        while head:
            ans.append(head.val)
            head = head.next

        ans.sort()
        head = l
        i = 0

        while head:
            head.val = ans[i]
            i += 1
            head = head.next
        head = l
        return head