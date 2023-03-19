class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        now = list(strs[0])
        used = [False] * len(strs[0])
        ans = 0
        for i, word in enumerate(strs):
            for j, ch in enumerate(word):
                if now[j] > ch and not used[j]:
                    used[j] = True
                    ans += 1
                now[j] = ch
        return ans