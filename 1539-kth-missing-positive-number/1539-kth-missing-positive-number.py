class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l = 0
        r = len(arr)
        while r - l > 1:
            m = (r + l) // 2
            if arr[m] - (m + 1) >= k:
                r = m
            else:
                l = m
        if k - (arr[l] - (l + 1)) <= 0:
            return k
        return k - (arr[l] - (l + 1)) + arr[l]