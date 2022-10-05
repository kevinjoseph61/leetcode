# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, left=root)
        
        def traverse(node, current_depth):
            if not node:
                return
            
            nonlocal depth
            if current_depth == depth:
                node.left = TreeNode(val, left=node.left, right=None)
                node.right = TreeNode(val, left=None, right=node.right)
                return
            else:
                traverse(node.right, current_depth + 1)
                traverse(node.left, current_depth + 1)
        
        traverse(root, 2)
        return root