class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        ans = []
        for alf in range(ord(s[0]) - ord("A"), ord(s[3]) - ord("A") + 1):
            for k in range(int(s[1]), int(s[4]) + 1):
                ans.append(chr(ord("A") + alf) + str(k))
        return ans