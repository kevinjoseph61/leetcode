# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        def generate(node, count):
            nonlocal ans
            if not node:
                return
            count ^= (1 << node.val)
            
            if node.left is None and node.right is None:
                if count & count-1 == 0:
                    ans += 1
                return
            
            generate(node.left, count)
            generate(node.right, count)
        
        ans = 0
        generate(root, 0)
        return ans