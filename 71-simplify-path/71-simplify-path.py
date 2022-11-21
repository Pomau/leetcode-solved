class Solution:
    def simplifyPath(self, path: str) -> str:
        answer = []
        word = ""
        for i in range(len(path) + 1):
            if i == len(path) or path[i] == "/":
                if word not in ["", "..", "."]:
                    answer.append(word)
                if word == ".." and len(answer) > 0:
                    answer.pop()
                word = ""
            else:
                word += path[i]
        return '/' + "/".join(answer)
            