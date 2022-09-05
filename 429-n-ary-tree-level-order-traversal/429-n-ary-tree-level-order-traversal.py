"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        levels = defaultdict(list)
        
        def traversal(node, level):
            if not node:
                return 
            levels[level].append(node.val)
            for i in node.children:
                traversal(i, level + 1)
        
        traversal(root, 0)
        return [levels[x] for x in sorted(levels)]