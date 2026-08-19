# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        ans = []

        while head:
            if head.val != val:
                ans.append(head.val)
            head = head.next

        root = None
        for i in ans:
            temp = ListNode(i)
            if root == None:
                root = temp
                head = temp
            else:
                root.next = temp
                root = root.next

        return head
        