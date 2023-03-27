class Solution:
    def minTimeToType(self, word: str) -> int:
        ans = 0
        now = "a"
        for ch in word:
            left = abs(ord(ch) - ord(now))
            if ord(ch) > ord(now):
                right = ord(now) - ord("a") + 1 + ord("z") - ord(ch)
            else:
                right = ord(ch) - ord("a") + 1 + ord("z") - ord(now)
            ans += min(left, right) + 1
            now = ch
        return ans