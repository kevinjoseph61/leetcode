# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def LCA(root):
            if not root:
                return None, False
            
            [n1, l] = LCA(root.left)
            [n2, r] = LCA(root.right)
            
            if n1 or n2:
                return (n1 or n2, True)
            
            if (l and r) or ((root == p or root == q) and (l or r)):
                return (root, True)
            else:
                if l or r or (root == p or root == q):
                    return (None, True)
            return (None, False)
        
        return LCA(root)[0]
            
            