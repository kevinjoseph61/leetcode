# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupLast = dummy
        
        while True:
            kth = self.getKth(groupLast, k)
            if not kth:
                break
            groupFirst = kth.next
            
            prev, curr = kth.next, groupLast.next
            while curr!=groupFirst:
                curr.next, prev, curr = prev, curr, curr.next
            
            groupLast.next, groupLast = kth, groupLast.next
        
        return dummy.next
        
    def getKth(self, curr, k):
        for i in range(k):
            if not curr:
                break
            curr = curr.next
        return curr
    