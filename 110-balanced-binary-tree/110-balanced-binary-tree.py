# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.flag = True
        try:
            depth = self.depth(root)
        except:
            pass
        return self.flag
        
    def depth(self, root):
        if root:
            l, r = self.depth(root.left), self.depth(root.right)
            if abs(l-r) > 1:
                self.flag = False
                raise KeyError
            return max(l, r) + 1
        else:
            return 0