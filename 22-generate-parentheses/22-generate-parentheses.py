class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.now = []
        return self.generate(2 * n, 0)
    def generate(self, n, o):
        if n == 0 or o < 0 or n < o:
            if o == 0:
                return [''.join(self.now)]
            return []
        answer = []
        self.now.append("(")
        answer += self.generate(n - 1, o + 1)
        self.now.pop()
        self.now.append(")")
        answer += self.generate(n - 1, o - 1)
        self.now.pop()
        return answer
