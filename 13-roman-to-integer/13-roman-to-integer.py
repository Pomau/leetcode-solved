class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        result = 0
        sign = 1
        for i in range(len(s)):
            if len(s) > i + 1 and (symbol[s[i]] > symbol[s[i + 1]] or symbol[s[i]] == symbol[s[i + 1]] and sign > 0) or len(s) == i + 1:
                result += symbol[s[i]]
                sign = 1
            elif len(s) > i + 1 and (symbol[s[i]] < symbol[s[i + 1]] or symbol[s[i]] == symbol[s[i + 1]] and sign < 0):
                sign = -1
                result -= symbol[s[i]]
        return result
                
        