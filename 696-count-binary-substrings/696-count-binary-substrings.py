class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans = 0
        count = [0, 0]
        for i in range(len(s)):
            num = int(s[i])
            count[num] += 1
            if i > 0 and s[i] != s[i - 1]:
                count[num] = 1
            ans += (count[num] <= count[1 - num])
        return ans