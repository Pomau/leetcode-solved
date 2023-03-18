class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        answer = [1]
        while rowIndex > 0:
            r = len(answer) - 1
            answer.append(1)
            while r > 0:
                answer[r] = answer[r] + answer[r - 1]
                r -= 1
            answer[0] = 1
            rowIndex -= 1
        return answer