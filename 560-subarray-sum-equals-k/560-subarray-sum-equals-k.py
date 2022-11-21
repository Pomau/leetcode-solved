class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = defaultdict(int)
        sums = 0
        answer = 0
        prefix_sums[0] = 1
        for i in range(len(nums)):
            sums += nums[i]
            answer += prefix_sums[sums - k]
            prefix_sums[sums] += 1
        return answer
