# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def traverse(node, s):
            if not node:
                return
            s = s - node.val
            if s == 0 and not node.left and not node.right:
                return True
            if traverse(node.left, s) or traverse(node.right, s):
                return True
            else:
                return False
        
        return traverse(root, targetSum)
            