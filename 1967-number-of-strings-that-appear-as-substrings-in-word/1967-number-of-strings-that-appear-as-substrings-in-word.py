class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        ans = 0
        for pattern in patterns:
            os = False
            alf = defaultdict(int)
            for ch in pattern:
                alf[ch] += 1 
            for r, ch in enumerate(word):
                alf[ch] -= 1
                if alf[ch] == 0:
                    del alf[ch]
                if r >= len(pattern):
                    alf[word[r - len(pattern)]] += 1
                    if alf[word[r - len(pattern)]] == 0:
                        del alf[word[r - len(pattern)]]
                if len(alf) == 0:
                    os = True
                    for i in range(len(pattern)):
                        if pattern[i] != word[r - len(pattern) + i + 1]:
                            os = False
                    if os:
                        break
            if os:
                ans += 1
        return ans