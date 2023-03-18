class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        answer = 0
        while r - l > 0:
            answer = max(answer, min(height[l], height[r]) * (r - l))
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        return answer
        