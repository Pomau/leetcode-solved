class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        ans = []
        nums.sort()
        prefix = [0]
        suffix = [0]
        for i in range(len(nums)):
            prefix.append(nums[i] + prefix[-1])
        for i in range(len(nums) - 1, -1, -1):
            suffix.append(nums[i] + suffix[-1])
        suffix.reverse()
        for q in queries:
            l = -1
            r = len(nums)
            while r - l > 1:
                m = (r + l) // 2
                if nums[m] <= q:
                    l = m
                else:
                    r = m 
            if l == -1:
                ans.append(prefix[-1] - q * len(nums))
            else:
                ans.append((l + 1) * q - prefix[l + 1] + suffix[l + 1] - (len(nums) - l - 1) * q)
        return ans