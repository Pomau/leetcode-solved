class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans = [[], []]
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        for num in nums1_set:
            if num not in nums2_set:
                ans[0].append(num)
        for num in nums2_set:
            if num not in nums1_set:
                ans[1].append(num)
        return ans