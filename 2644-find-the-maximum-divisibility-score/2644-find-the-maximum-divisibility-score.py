class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        counts = [0] * len(divisors)
        for i, num in enumerate(nums):
            for j, div in enumerate(divisors):
                if num % div == 0:
                    counts[j] += 1
        ans = 0
        for i in range(len(counts)):
            if counts[i] > counts[ans] or counts[i] == counts[ans] and divisors[i] < divisors[ans]:
                ans = i
        return divisors[ans]