class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend == -2147483648 and divisor == -1): return 2147483647
        minus = 1
        if (dividend > 0 and divisor < 0) or (divisor > 0 and dividend < 0):
            minus = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        a = [divisor]
        koef = [1]
        while a[-1] < dividend:
            a.append(a[-1] + a[-1])
            koef.append(koef[-1] + koef[-1])
        l = len(a) - 1
        answer = 0
        while l >= 0:
            if a[l] > dividend:
                l -= 1
            else:
                answer += koef[l]
                dividend -= a[l]
        return minus * answer