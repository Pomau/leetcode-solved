class Solution:
    def findComplement(self, num: int) -> int:
        answer = 0
        x = num
        k = 1
        while x > 0:
            answer += (1 - x % 2) * k
            k *= 2
            x //= 2
        return answer