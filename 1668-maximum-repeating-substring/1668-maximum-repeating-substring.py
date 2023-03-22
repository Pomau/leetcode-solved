class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        ans = 0
        for i in range(len(sequence)):
            l = i
            now = 0
            while sequence[l:l + len(word)] == word:
                l += len(word)
                now += 1
            ans = max(ans, now)
        return ans