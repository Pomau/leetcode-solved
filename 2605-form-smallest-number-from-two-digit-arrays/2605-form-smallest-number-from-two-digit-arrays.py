class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        alf = set(nums1)
        alf2 = set(nums2)
        mink = float("inf")
        for i in alf:
            if i in alf2:
                mink = min(mink, i)
        if mink != float("inf"):
            return mink
        a  = [min(nums1), min(nums2)]
        a.sort()
        if a[0] == 0:
            a[0], a[1] = a[1], a[0]
        return a[0] * 10 + a[1]
        