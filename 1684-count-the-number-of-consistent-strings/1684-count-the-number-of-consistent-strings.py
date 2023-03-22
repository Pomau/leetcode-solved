class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        alf = set(allowed)
        ans = 0
        for word in words:
            os = True
            for ch in word:
                if ch not in alf:
                    os = False
                    break
            if os:
                ans += 1
        return ans