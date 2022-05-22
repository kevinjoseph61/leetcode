# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.dict = {}
        self.trav(root, 0)
        if not self.dict:
            return []
        res = []
        for i in range(max(self.dict.keys())+1):
            res.append(self.dict[i])
        return res
    
    def trav(self, root, level):
        if root:
            self.trav(root.left, level+1)
            self.dict[level]= root.val
            self.trav(root.right, level+1)