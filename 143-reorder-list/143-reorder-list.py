# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        
        curr = slow.next
        prev = slow.next = None
        
        
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        
        curr = head
        
        while curr and prev:
            curr.next, prev.next, curr, prev = prev, curr.next, curr.next, prev.next
            
        #if prev:
            
            
        return head
        