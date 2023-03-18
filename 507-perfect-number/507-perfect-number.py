class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        l = 1
        ans = -num
        while l * l <= num:
            if num % l == 0:
                ans += l + num // l
            l += 1
        return ans == num