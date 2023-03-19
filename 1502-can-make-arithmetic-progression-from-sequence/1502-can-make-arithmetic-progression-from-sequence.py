class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        nums = defaultdict(bool)
        maxn = max(arr)
        minn = min(arr)
        kf = (maxn - minn) / (len(arr) - 1)
        for num in arr:
            nums[num] = True
        for i in range(1, len(arr) - 1):
            if nums[minn + i * kf] == False:
                return False
        return True
        