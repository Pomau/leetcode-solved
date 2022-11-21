class Solution:
    def reverseWords(self, s: str) -> str:
        answer = ""
        word = []
        for l in range(len(s) + 1):
            if l == len(s) or s[l] == " ":
                if len(word) != 0:
                    word.reverse()
                    answer += ''.join(word)
                    word = []
                answer +=  " "
            else:
                word.append(s[l])
        return answer[:-1]
        