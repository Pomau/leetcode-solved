class Solution:
    def addMinimum(self, word: str) -> int:
        ans = 0
        last = 2
        for i, ch in enumerate(word):
            ind = ord(ch) - ord("a")
            # print(word, i,  ind, last)
            if ind > last:
                if ind - 1 != last:
                    ans += 1
            else:
                ans += 2 - last
                ans += ind
            last = ind
        ans += 2 - last
        return ans
                