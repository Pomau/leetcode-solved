class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        alf = defaultdict(int)
        for ch in needle:
            alf[ch] += 1
        for i, el in enumerate(haystack):
            alf[el] -= 1
            if alf[el] == 0:
                del alf[el]
            if i - len(needle) >= 0:
                alf[haystack[i - len(needle)]] += 1
                if alf[haystack[i - len(needle)]] == 0:
                    del alf[haystack[i - len(needle)]]
            if len(alf) == 0:
                check = True
                for j in range(i - len(needle) + 1, i + 1):
                    if haystack[j] != needle[j - (i - len(needle) + 1)]:
                        check = False
                        break
                if check:
                    return i - len(needle) + 1
        return -1