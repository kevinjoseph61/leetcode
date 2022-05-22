# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 1
        self.check(root.val, root.left)
        self.check(root.val, root.right)
        return self.count
        
    def check(self, gtSoFar, node):
        if node:
            if node.val >= gtSoFar:
                self.count += 1
                gtSoFar = node.val
            self.check(gtSoFar, node.left)
            self.check(gtSoFar, node.right)
                