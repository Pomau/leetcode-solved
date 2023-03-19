class Solution:
    def findLucky(self, arr: List[int]) -> int:
        alf = defaultdict(int)
        for num in arr:
            alf[num] += 1
        ans = -1
        for key, item in alf.items():
            if key == item and ans < key:
                ans = key
        return ans