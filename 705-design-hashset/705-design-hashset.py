class Node:
    def __init__(self, val=None,next=None, slow =None):
        self.val = val
        self.next = None
class MyHashSet:
    def __init__(self):
        self.arr = [Node() for _ in range(10**3)]

    def add(self, key: int) -> None:
        node = self.arr[self.hash(key)]
        last = None
        while node != None and node.val != key:
            last = node
            node = node.next
        if node != None and node.val == key:
            return 
        last.next = Node(key)

    def remove(self, key: int) -> None:
        node = self.arr[self.hash(key)]
        last = None
        while node != None and node.val != key:
            last = node
            node = node.next
        if node != None and node.val == key:
            last.next = node.next

    def contains(self, key: int) -> bool:
        node = self.arr[self.hash(key)]
        last = None
        while node != None and node.val != key:
            last = node
            node = node.next
        if node != None and node.val == key:
            return True
        return False
    def hash(self, key):
        key_s = key*1031237
        ans = 0
        while key_s > 0:
            ans = (ans * 71 + key_s%10) % len(self.arr)
            key_s //= 10
        return ans


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)