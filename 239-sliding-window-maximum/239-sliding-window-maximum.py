class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = Queue()
        answer = []
        for r in range(len(nums)):
            queue.push(nums[r])
            if r >= k:
                queue.pop()
            if r + 1 >= k:
                answer.append(queue.get_max())
        return answer
            
            
            
class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.infinity = -(10**10)
        self.max_stack1 = [self.infinity]
        self.max_stack2 = [self.infinity]
    
    def push(self, x):
        self.stack1.append(x)
        self.max_stack1.append(max(self.max_stack1[-1], x))
    
    def pop(self):
        self.moving()
        if len(self.stack2) > 0:
            self.stack2.pop()
            self.max_stack2.pop()    
    
    def moving(self):
        if len(self.stack2) == 0:
            for i in range(len(self.stack1) - 1, -1, -1):
                element = self.stack1[i]
                self.stack2.append(element)
                self.max_stack2.append(max(self.max_stack2[-1], element))
                self.stack1.pop()
                self.max_stack1.pop()    
        
    
    def get_max(self):
        maxn = self.infinity
        if len(self.max_stack1) > 0:
            maxn = max(maxn, self.max_stack1[-1])
        if len(self.max_stack2) > 0:
            maxn = max(maxn, self.max_stack2[-1])
        return maxn
        
                
        