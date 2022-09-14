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
            count[node.val - 1] += 1
            
            if node.left is None and node.right is None:
                odd = False
                for i in count:
                    if i % 2 == 1:
                        if odd:
                            return
                        else:
                            odd = True
                ans += 1
                
            countR = count.copy()
            generate(node.left, count)
            generate(node.right, countR)
        
        ans = 0
        generate(root, [0, 0, 0, 0, 0, 0, 0, 0, 0])
        return ans