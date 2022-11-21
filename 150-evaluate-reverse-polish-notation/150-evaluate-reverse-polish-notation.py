class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        arr = []
        for token in tokens:
            if token.isdigit() or len(token) > 1:
                if len(token) > 1 and token[0] == "-":
                    arr.append(-1 * int(token[1:]))
                else:
                    arr.append(int(token))
            else:
                num2 = arr.pop()
                num1 = arr.pop()
                answer = 0
                if token == "+":
                    answer = num1 + num2
                elif token == "*":
                    answer = num1 * num2
                elif token == '/':  
                    answer = abs(num1) // abs(num2)
                    if num1 < 0:
                        answer *= -1
                    if num2 < 0:
                        answer *= -1
                elif token == "-":
                    answer = num1 - num2
                arr.append(answer)
        return arr[-1]