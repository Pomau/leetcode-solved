class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        answer = []
        l1 = 0
        l2 = 0
        while len(answer) != n + m:
            if l1 < m and (l2 >= n or nums1[l1] <= nums2[l2]):
                answer.append(nums1[l1])
                l1 += 1
            else:
                answer.append(nums2[l2])
                l2 += 1
        for i in range(len(answer)):
            nums1[i] = answer[i]
        