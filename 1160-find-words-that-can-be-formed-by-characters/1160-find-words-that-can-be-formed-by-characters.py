class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        for word in words:
            alf = defaultdict(int)
            for ch in chars:
                alf[ch] += 1
            os = True
            for i in word:
                alf[i] -= 1
                if alf[i] < 0:
                    os = False
            if os:
                ans += len(word)
        return ans
        