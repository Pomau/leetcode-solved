class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        sign = 1
        s = s.strip()
        for i in range(0, len(s)):
            char = s[i]
            if char.isdigit():
                res = res * 10 + int(char)
            elif (char == "+" or char == "-") and i == 0:
                if char == "-":
                    sign = -1
            else:
                break
        res *= sign
        res = min(2**31 - 1, res)
        res = max(-2**31, res)
        return res
                
        