class Solution:
    def interpret(self, command: str) -> str:
        r = 0
        answer = []
        while r < len(command):
            if command[r] == "G":
                answer.append("G")
            elif command[r + 1] == ")":
                answer.append("o")
                r += 1
            else:
                answer.append("al")
                r += 3
            r += 1
        return ''.join(answer)