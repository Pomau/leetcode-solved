class Solution:
    def reorderSpaces(self, text: str) -> str:
        ans = []
        count = 0
        word = []
        for i, ch in enumerate(text):
            if ch != " ":
                word.append(ch)
            else:
                count += 1
            if (ch == " " or len(text) == i + 1) and len(word) > 0:
                ans.append("".join(word))
                word = []
        if len(ans) == 1:
            return ans[0] + " " * count
        return (" " * (count // (len(ans) - 1))).join(ans) + " " * (count % (len(ans) - 1))
                