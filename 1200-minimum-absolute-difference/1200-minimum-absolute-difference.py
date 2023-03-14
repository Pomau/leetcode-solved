class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mink = arr[1] - arr[0]
        ans = []
        for i, num in enumerate(arr):
            if i == 0:
                continue
            if mink > num - arr[i - 1]:
                mink = num - arr[i - 1]
                ans = []
            if mink == num - arr[i - 1]:
                ans.append([arr[i - 1], num])
        return ans
                
                