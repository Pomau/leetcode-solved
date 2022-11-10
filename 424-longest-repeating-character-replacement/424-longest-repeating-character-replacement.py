class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        answer = 0
        max_count_ch = 'A'
        alf = defaultdict(int)
        for r in range(len(s)):
            alf[s[r]] += 1
            if alf[max_count_ch] <= alf[s[r]]:
                max_count_ch = s[r]
            while r - l + 1 - alf[max_count_ch] > k:
                alf[s[l]] -= 1
                if alf[s[l]] == 0:
                    del alf[s[l]]
                if max_count_ch == s[l]:
                    for ch in alf:
                        if alf[max_count_ch] <= alf[ch]:
                            max_count_ch = ch
                l += 1
            answer = max(answer, r - l + 1)
        return answer