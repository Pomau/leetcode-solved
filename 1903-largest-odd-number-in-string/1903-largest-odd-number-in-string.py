class Solution:
    def largestOddNumber(self, num: str) -> str:
        ind = len(num) - 1
        while ind >= 0 and int(num[ind]) % 2 == 0:
            ind -= 1
        if ind == -1:
            return ""
        return num[:ind + 1]