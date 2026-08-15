# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hs = set()
        while(head!=None):
            if head in hs:
                return True
            hs.add(head)
            head=head.next
        return False
        