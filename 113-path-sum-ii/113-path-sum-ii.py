# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
            ans = []
            
            def traverse(node, s, curr):
                if not node:
                    return
                #print(node.val, s, curr)
                curr.append(node.val)
                s += node.val                
                if node.left is None and node.right is None and s == targetSum:
                    ans.append(curr)
                traverse(node.left, s, curr[::])
                traverse(node.right, s, curr[::])
                
            traverse(root, 0, [])
            return ans
                    
                