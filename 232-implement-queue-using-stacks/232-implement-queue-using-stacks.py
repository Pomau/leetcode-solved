class MyQueue:

    def __init__(self):
        self.arr_insert = []
        self.arr_remove = []

    def push(self, x: int) -> None:
        self.arr_insert.append(x)
        

    def pop(self) -> int:
        self.merge()
        return self.arr_remove.pop()
        

    def merge(self) -> None:
        if len(self.arr_remove) != 0:
            return 
        while len(self.arr_insert) > 0:
            back = self.arr_insert.pop()
            self.arr_remove.append(back)

        

    def peek(self) -> int:
        self.merge()
        return self.arr_remove[-1]

    def empty(self) -> bool:
        return (len(self.arr_remove) + len(self.arr_insert) == 0)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()