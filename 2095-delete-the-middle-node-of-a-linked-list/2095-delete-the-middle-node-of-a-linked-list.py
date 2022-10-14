# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        p, s, f = None, head, head
        while f and f.next:
            p, s, f = s, s.next, f.next.next
        p.next = s.next
        return head
        
        