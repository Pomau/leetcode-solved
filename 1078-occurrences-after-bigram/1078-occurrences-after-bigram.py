class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        ans = []
        last = []
        word = []
        for i, ch in enumerate(text):
            if ch != " ":
                word.append(ch)
            if (ch == " " or i == len(text) - 1) and len(word) > 0:
                now = "".join(word)
                if len(last) > 1 and last[-1] == second and last[-2] == first:
                    ans.append(now)
                last.append(now)
                word = []
        return ans