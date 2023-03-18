class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        alf = defaultdict(int)
        for num in nums1:
            alf[num] = 1
        answer = []
        for num in nums2:
            alf[num] -= 1
            if alf[num] >= 0:
                answer.append(num)
        return answer