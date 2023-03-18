class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        answer = 0
        if y > x:
            x, y = y, x
        while x > 0 or y > 0:
            if y % 2 != x % 2:
                answer += 1
            x = x // 2
            y = y // 2
        return answer

