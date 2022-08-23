# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        front = head
        def helper(node):
            if not node:
                return True
            equal = helper(node.next)
            nonlocal front
            equal_so_far = (node.val == front.val)
            front = front.next
            
            return equal and equal_so_far
        
        return helper(head)