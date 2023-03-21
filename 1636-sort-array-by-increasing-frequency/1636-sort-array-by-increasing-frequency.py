class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        alf = defaultdict(int)
        for num in nums:
            alf[num] += 1
        arr = []
        for key, item in alf.items():
            arr.append([item, -key])
        arr.sort()
        ans = []
        for i in range(len(arr)):
            ans += [-arr[i][1]] * arr[i][0]
        return ans