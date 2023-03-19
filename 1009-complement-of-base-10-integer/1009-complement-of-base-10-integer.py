class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        answer = 0
        x = n
        k = 1
        while x > 0:
            answer += (1 - x % 2) * k
            k *= 2
            x //= 2
        return answer