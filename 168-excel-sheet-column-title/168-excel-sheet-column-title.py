class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        answer = []
        while columnNumber > 0:
            columnNumber -= 1
            answer.append(chr(ord("A") + columnNumber % 26))
            columnNumber //= 26
        answer.reverse()
        return "".join(answer)