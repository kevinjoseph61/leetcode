# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        leveldict = defaultdict(list)
        
        def traverse(node, level):
            if not node:
                return
            leveldict[level].append(node.val)
            traverse(node.left, level+1)
            traverse(node.right, level+1)
        
        traverse(root, 0)
        ans = []
        for i in sorted(leveldict):
            ans.append(sum(leveldict[i])/len(leveldict[i]))
        return ans