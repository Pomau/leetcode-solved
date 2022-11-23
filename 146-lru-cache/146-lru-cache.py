class Node:
    def __init__(self, key=None, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
        self.key = key
        
class ListNode:
    def __init__(self):
        self.head = Node()
        self.tail = Node(prev=self.head)
        self.head.next = self.tail
    
    def insert(self, key, val):
        now = Node(key, val, self.head.next, self.head)
        self.head.next.prev = now
        self.head.next = now
        return now
    
    def delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
        
class LRUCache:
    def __init__(self, capacity: int):
        self.nodes = ListNode()
        self.arr = dict()
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key not in self.arr:
            return -1
        return self.update(key, self.arr[key].val).val
        

    def put(self, key: int, value: int) -> None:
        if key in self.arr:
            self.update(key, value)
        else:
            if len(self.arr) >= self.capacity:
                self.deletelast()
            self.update(key, value)
            
        
    def update(self, key, val):
        if key in self.arr:
            node = self.arr[key]
            self.nodes.delete(node)
        self.arr[key] = self.nodes.insert(key, val)
        return self.arr[key]
    
    def deletelast(self):
        last = self.nodes.tail.prev
        self.nodes.delete(last)
        del self.arr[last.key]
        
    
        
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)