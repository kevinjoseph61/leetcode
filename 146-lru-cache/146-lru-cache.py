class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
        self.map = {}
        
    def insert(self, node):
        #node.next = node.prev = None
        prev, next = self.right.prev, self.right
        node.next, node.prev = next, prev
        next.prev = prev.next = node
    
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def get(self, key: int) -> int:
        res = -1
        if key in self.map:
            res = self.map[key].value
            self.remove(self.map[key])
            self.insert(self.map[key])
        return res

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(self.map[key])
        node = Node(key, value)
        self.map[key] = node
        self.insert(node)
        if len(self.map) > self.cap:
            lru = self.left.next
            del self.map[lru.key]
            self.remove(lru)
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)