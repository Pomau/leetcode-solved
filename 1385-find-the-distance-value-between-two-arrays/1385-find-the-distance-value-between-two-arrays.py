class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr1.sort()
        arr2.sort()
        l = 0
        r = 0
        ans = 0
        for i, el in enumerate(arr1):
            while l + 1 < len(arr2) and arr2[l + 1] < el:
                l += 1
            while r < len(arr2) and arr2[r] < el:
                r += 1
            if not (0 <= l < len(arr2) and abs(el - arr2[l]) <= d or 0 <= r < len(arr2) and abs(el - arr2[r]) <= d) and (0 <= l < len(arr2) or 0 <= r < len(arr2)):
                ans += 1
        return ans