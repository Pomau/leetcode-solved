class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        arr = [height for height in heights]
        arr.sort()
        ans = 0
        for i in range(len(heights)):
            if heights[i] != arr[i]:
                ans += 1
        return ans