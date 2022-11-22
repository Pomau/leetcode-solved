class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class RandomizedSet:

    def __init__(self):
        self.our = dict()
        self.arr = []
        self.l = 0
        

    def insert(self, val: int) -> bool:
        if val in self.our:
            return False
        self.our[val] = len(self.arr)
        self.arr.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.our:
            return False 
        index = self.our[val]
        self.our[self.arr[self.l]] = index
        del self.our[val]
        self.arr[self.l], self.arr[index] = self.arr[index], self.arr[self.l]
        self.l += 1
        if len(self.our) < self.l:
            arr = []
            for i in range(self.l, len(self.arr)):
                arr.append(self.arr[i])
                self.our[self.arr[i]] = len(arr) - 1
            self.arr = arr
            self.l = 0
        return True
    

    def getRandom(self) -> int:
        return self.arr[randint(self.l, len(self.arr) - 1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()