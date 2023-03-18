class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        answer = []
        word = []
        for r in range(len(s) - 1, -1, -1):
            if s[r] != "-":
                word.append(s[r])
                if len(word) == k:
                    word.reverse()
                    answer.append(''.join(word))
                    word = []
        if len(word) != 0:
            word.reverse()
            answer.append(''.join(word))
        answer.reverse()
        return '-'.join(answer).upper()