class Solution:
    def capitalizeTitle(self, title: str) -> str:
        ans = []
        word = []
        for i, ch in enumerate(title):
            if ch != " ":
                word.append(ch.lower())
            if (ch == " " or i == len(title) - 1) and len(word) > 0:
                ans.append("".join(word))
                if len(word) > 2:
                    ans[-1] = ans[-1][0].upper() + ans[-1][1:]
                word = []
        return " ".join(ans)