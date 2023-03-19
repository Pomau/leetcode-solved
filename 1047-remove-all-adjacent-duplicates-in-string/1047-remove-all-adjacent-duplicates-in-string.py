class Solution:
    def removeDuplicates(self, s: str) -> str:
        arr = []
        for i, ch in enumerate(s):
            if len(arr) > 0 and ch == arr[-1]:
                arr.pop()
            else:
                arr.append(ch)
        return "".join(arr)