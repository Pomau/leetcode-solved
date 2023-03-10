class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        ans = []
        l = 0
        for r, ch in enumerate(s):
            if ch != s[l]:
                if r - l >= 3:
                    ans.append([l, r - 1])
                l = r
        if r  - l + 1 >= 3:
            ans.append([l, r])
        return ans