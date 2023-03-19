class Node:
    def __init__(self, key=None, val=None, next=None):
        self.val = val
        self.key = key
        self.next = None
class MyHashMap:

    def __init__(self):
        self.arr = [Node() for _ in range(10**5)]

    def put(self, key: int, value: int) -> None:
        node = self.arr[self.hash(key)]
        last = None
        while node != None and node.key != key:
            last = node
            node = node.next
        if node != None and node.key == key:
            node.val = value 
            return
        last.next = Node(key, value)
        

    def get(self, key: int) -> int:
        node = self.arr[self.hash(key)]
        last = None
        while node != None and node.key != key:
            last = node
            node = node.next
        if node != None and node.key == key:
            return node.val
        return -1
        

    def remove(self, key: int) -> None:
        node = self.arr[self.hash(key)]
        last = None
        while node != None and node.key != key:
            last = node
            node = node.next
        if node != None and node.key == key:
            last.next = node.next 
    def hash(self, key):
        key_s = key*1031237
        ans = 0
        while key_s > 0:
            ans = (ans * 71 + key_s%10) % len(self.arr)
            key_s //= 10
        return ans

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)