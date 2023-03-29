class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ans = []
        first = False
        for i, char in enumerate(word):
            ans.append(char)
            if char == ch and not first: 
                ans.reverse()
                first = True
        return "".join(ans)