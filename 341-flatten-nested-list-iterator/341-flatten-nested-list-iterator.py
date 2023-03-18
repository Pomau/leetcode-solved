# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = [[nestedList, 0]]
    
    def next(self) -> int:
        number = self.stack[-1][0][self.stack[-1][1]].getInteger()
        self.stack[-1][1] += 1
        return number
        
    def hasNext(self) -> bool:
        while len(self.stack) > 0:
            arr = self.stack[-1][0]
            number = self.stack[-1][1]
            if number >= len(arr):
                self.stack.pop()
                if len(self.stack) > 0:
                    self.stack[-1][1] += 1
                continue
            if arr[number].isInteger():
                return True
            else:
                self.stack.append([arr[number].getList(), 0])
        return False

                

         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())