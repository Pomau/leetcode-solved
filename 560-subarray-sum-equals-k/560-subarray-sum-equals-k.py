class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        answer = 0
        trains = defaultdict(int)
        sums = 0
        trains[0] = 1
        for i in range(len(nums)):
            sums += nums[i]
            answer += trains[sums - k]
            trains[sums] += 1
        return answer
            