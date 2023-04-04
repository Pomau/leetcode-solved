class Solution:
    def partitionString(self, s: str) -> int:
        alf = set()
        l = 0
        ans = 0
        for r, ch in enumerate(s):
            if ch in alf:
                l = r
                ans += 1
                alf = set()
            alf.add(ch)
        return ans + 1