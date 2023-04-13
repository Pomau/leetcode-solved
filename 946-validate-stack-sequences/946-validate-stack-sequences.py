class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        l = 0
        for i, el in enumerate(popped):
            if len(stack) > 0 and stack[-1] == el:
                stack.pop()
                continue
            while l < len(pushed) and pushed[l] != el:
                stack.append(pushed[l])
                l += 1
            if not (l < len(pushed) and pushed[l] == el):
                return False
            else:
                l += 1
        return len(stack) == 0