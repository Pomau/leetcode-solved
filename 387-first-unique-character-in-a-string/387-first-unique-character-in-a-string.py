class Solution:
    def firstUniqChar(self, s: str) -> int:
        alf = defaultdict(int)
        for i in s:
            alf[i] += 1
        for i in range(len(s)):
            if alf[s[i]] == 1:
                return i
        return -1
        