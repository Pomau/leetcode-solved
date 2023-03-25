class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        alf = defaultdict(int)
        now = -1
        for r in range(len(word)):
            if word[r].isdigit():
                if now == -1:
                    now = 0
                now = now * 10 + int(word[r])
            if (not word[r].isdigit() or r == len(word) - 1) and now != -1:
                alf[now] = 1
                now = -1
        return len(alf)