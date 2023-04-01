class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        for i, num in enumerate(nums):
            if i % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        odd.sort(reverse=True)
        even.sort()
        ans = []
        for i in range(len(nums)):
            if i % 2 == 0:
                ans.append(even[i // 2])
            else:
                ans.append(odd[i//2])
        return ans