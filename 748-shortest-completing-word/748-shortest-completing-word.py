class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        ans = "x" * 100
        for word in words:
            alf = defaultdict(int)
            for ch in licensePlate:
                if ch.isalpha():
                    alf[ch.lower()] += 1
            for ch in word:
                if ch.lower() in alf:
                    alf[ch.lower()] -= 1
                    if alf[ch.lower()] == 0:
                        del alf[ch.lower()]
            if len(alf) == 0:
                ans = min(ans, word, key=len)
        return ans