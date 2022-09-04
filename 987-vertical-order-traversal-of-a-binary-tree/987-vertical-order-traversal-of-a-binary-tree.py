# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from sortedcontainers import SortedList
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = defaultdict(SortedList)
        
        def traverse(node, levelh, levelv):
            if not node:
                return
            levels[levelh].add([levelv, node.val])
            traverse(node.left, levelh - 1, levelv + 1)
            traverse(node.right, levelh + 1, levelv + 1)
        
        traverse(root, 0, 0)
        return [[y[1] for y in (levels[x])] for x in sorted(levels)]
        