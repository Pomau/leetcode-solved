class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        answer = []
        min = ""
        if num < 0:
            min = "-"
            num *= -1
        while num > 0:
            answer.append(str(num%7))
            num //=7
        answer.append(min)
        answer.reverse()
        return ''.join(answer)