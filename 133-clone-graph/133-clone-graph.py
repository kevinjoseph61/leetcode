"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        map = defaultdict(Node)
        self.duplicate(node, map)
        self.copied = {}
        return self.copy(node, map)
        
    def duplicate(self, node, map):
        map[node].val = node.val
        for i in node.neighbors:
            if i not in map:
                self.duplicate(i, map)
                
    def copy(self, node, map):
        c = map[node]
        self.copied[node] = c
        for i in node.neighbors:
            if i not in self.copied:
                c.neighbors.append(self.copy(i, map))
            else:
                c.neighbors.append(self.copied[i])
        return c
    