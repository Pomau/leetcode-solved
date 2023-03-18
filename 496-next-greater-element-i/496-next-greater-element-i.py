class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        alf = defaultdict(int)
        nums2_gte = [-1] * len(nums2)
        steak = []
        for i, el in enumerate(nums2):
            alf[el] = i
            while len(steak) > 0 and nums2[steak[-1]] < el:
                nums2_gte[steak[-1]] = el
                steak.pop()
            steak.append(i)
        answer = []
        for el in nums1:
            i = alf[el]
            answer.append(nums2_gte[i])
        return answer