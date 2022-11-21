class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        transfer = 0
        answer = []
        n = max(len(num1), len(num2))
        for i in range(n):
            if i < len(num1):
                transfer +=  int(num1[len(num1) - i - 1]) 
            if i < len(num2):
                transfer +=  int(num2[len(num2) - i - 1])
            answer.append(str(transfer % 10))
            transfer = transfer // 10
        if transfer > 0:
            answer.append(str(transfer))
        answer.reverse()
        return ''.join(answer)