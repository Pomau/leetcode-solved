class Solution:
    def isHappy(self, n: int) -> bool:
        number_history = set()
        while n > 1:
            next = 0
            number = n
            while number > 0:
                next += (number % 10) ** 2
                number //= 10
            if next in number_history:
                return False
            number_history.add(next)
            n = next
        return True
            