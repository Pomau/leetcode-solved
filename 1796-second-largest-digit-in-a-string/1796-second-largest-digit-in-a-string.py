class Solution:
    def secondHighest(self, s: str) -> int:
        digit = [0] * 10
        for i, ch in enumerate(s):
            if ch.isdigit():
                digit[ord(ch) - ord("0")] += 1
        status = 0
        for i in range(9, -1, -1):
            if digit[i] != 0:
                if status == 0:
                    status = 1
                else:
                    return i
        return -1