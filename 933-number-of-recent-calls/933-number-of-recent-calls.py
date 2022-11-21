class RecentCounter:

    def __init__(self):
        self.q = Queue()

    def ping(self, t: int) -> int:
        self.q.insert(t)
        while t - self.q.back() > 3000:
            self.q.remove()
        return self.q.len()
    
        

class Queue:
    def __init__(self):
        self.arr_insert = []
        self.arr_remove = []
    
    def insert(self, t):
        self.arr_insert.append(t)
    
    def remove(self):
        self.merge()
        return self.arr_remove.pop()
    
    def back(self):
        self.merge()
        return self.arr_remove[-1]
        
    def merge(self):
        if len(self.arr_remove) != 0:
            return
        while len(self.arr_insert) > 0:
            back = self.arr_insert.pop()
            self.arr_remove.append(back)
    
    def len(self):
        return len(self.arr_insert) + len(self.arr_remove)
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)