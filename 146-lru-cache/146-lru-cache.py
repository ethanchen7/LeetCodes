class Node:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        
        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def add(self, node): # move to the head (MRU)
        head_next = self.head.next
        head_next.prev = node
        
        self.head.next = node
        
        node.prev = self.head
        node.next = head_next
    
    def remove(self, node):
        node_next = node.next
        node_prev = node.prev
        
        node_prev.next = node_next
        node_next.prev = node_prev

    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove(node)
        self.add(node)
        return node.val
        
    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            old_node = self.cache[key]
            self.remove(old_node)
        
        new_node = Node(key, value)
        self.cache[key] = new_node
        self.add(new_node)
        
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            del self.cache[lru.key]
            self.remove(lru)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)