class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        x_str = str(x)
        if x < 0:
            sign = -1
            x_str = x_str[1:]
        result = sign * int(x_str[::-1])
        if -1 * 2**31 <= result < 2 ** 31:
            return result
        else:
            return 0