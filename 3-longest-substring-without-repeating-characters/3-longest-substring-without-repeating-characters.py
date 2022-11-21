class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        alf = set()
        l = 0
        answer = 0
        for r in range(len(s)):
            while s[r] in alf:
                alf.discard(s[l])
                l += 1
            alf.add(s[r])
            answer = max(answer, r - l + 1)
        return answer