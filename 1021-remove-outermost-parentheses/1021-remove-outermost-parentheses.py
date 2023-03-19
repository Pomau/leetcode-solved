class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        answer = []
        stack = []
        for ch in s:
            if ch == "(":
                stack.append(ch)
                if len(stack) > 1:
                    answer.append(ch)
            else:
                stack.pop()
                if len(stack) >= 1:
                    answer.append(ch)
        return "".join(answer)