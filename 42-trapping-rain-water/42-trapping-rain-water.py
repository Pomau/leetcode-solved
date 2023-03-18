class Solution:
    def trap(self, height: List[int]) -> int:
        max_index = 0
        for i in range(len(height)):
            if height[i] >= height[max_index]:
                max_index = i
        answer = 0
        sums = 0
        l = 0
        for r in range(1, max_index + 1):
            if height[r] >= height[l]:
                answer += sums
                l = r
                sums = 0
            else:
                sums += height[l] - height[r]
        sums = 0
        l = len(height) - 1
        for r in range(len(height) - 2, max_index - 1, -1):
            if height[r] >= height[l]:
                answer += sums
                l = r
                sums = 0
            else:
                sums += height[l] - height[r]
        return answer


        