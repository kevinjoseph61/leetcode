# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr = head
        p = None
        pos = 1
        while(curr):
            if pos == left:
                break
            p = curr
            curr = curr.next
            pos += 1
        l = curr
        while(curr):
            if pos == right:
                break
            curr = curr.next
            pos += 1
        
        r = curr
        n = r.next
        
        if r: r.next = None
        curr = l
        prev = None
        while(curr):
            curr.next, curr, prev = prev, curr.next, curr
        
        if p: p.next = r
        l.next = n
        
        if head == l:
            head = r
        
        return head