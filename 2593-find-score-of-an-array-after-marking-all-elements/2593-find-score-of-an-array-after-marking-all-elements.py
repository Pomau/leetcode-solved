class Solution:
    def findScore(self, nums: List[int]) -> int:
        used = [False] * len(nums)
        count = 0
        arr = [[nums[i], i] for i in range(len(nums))]
        l = 0
        arr.sort()
        ans = 0
        while count < len(nums):
            while used[arr[l][1]]:
                l += 1
            now = arr[l][1]
            for k in range(-1, 2):
                if 0 <= now + k < len(used) and not used[now + k]:
                    used[now + k]= True
                    count += 1
            ans += arr[l][0]
        return ans