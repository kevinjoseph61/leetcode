# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.m = float(-inf)
        self.traverse(root)
        return self.m
        
    def traverse(self, node):
        if node:
            l, r = self.traverse(node.left), self.traverse(node.right)
            self.m = max(l + r + node.val, node.val, r + node.val, l + node.val, self.m)
            return max(l, r, 0) + node.val
        return 0