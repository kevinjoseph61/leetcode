# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        ans = []
        
        def traverse(node):
            if not node:
                return
            ans.append(str(node.val))
            if node.left or node.right:
                ans.append('(')
                traverse(node.left)
                ans.append(')')
            if node.right:
                ans.append('(')
                traverse(node.right)
                ans.append(')')
        
        traverse(root)
        return ''.join(ans)