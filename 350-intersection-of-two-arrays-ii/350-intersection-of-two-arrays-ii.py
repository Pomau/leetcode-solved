class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_dict = defaultdict(int)
        for num in nums1:
            nums1_dict[num] += 1
        answer = []
        for num in nums2:
            if nums1_dict[num] > 0:
                 answer.append(num)
                 nums1_dict[num] -= 1
        return answer
