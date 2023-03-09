class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        answer = 0
        for i, num in enumerate(nums):
            if k > 0:
                if num >= 0 or len(nums) == i + 1:
                    if k % 2 == 0:
                        answer += num
                    else:
                        answer -= num
                    k = 0
                else:
                    if i + 1 < len(nums) and k % 2 == 0 and abs(num) < abs(nums[i + 1]):
                        answer += num
                        k = 0
                    else:
                        answer -= num
                        k -= 1
                            
            else:
                answer += num
        return answer