# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.valid = True
        self.check(root)
        return self.valid
        
    def check(self, node):
        if node:
            ll, lg = self.check(node.left)
            rl, rg = self.check(node.right)
            if lg >= node.val or rl <= node.val:
                self.valid = False
            return min(node.val, ll, rl), max(node.val, lg, rg)
        return float(inf), float(-inf)