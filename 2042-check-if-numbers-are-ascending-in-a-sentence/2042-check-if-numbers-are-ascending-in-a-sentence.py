class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        word = []
        last = -1
        for i, ch in enumerate(s):
            if ch != " ":
                word.append(ch)
            if (ch == " " or i == len(s) - 1) and len(word) > 0:
                word1 = "".join(word)
                if word1.isdigit():
                    if int(word1) > last:
                        last = int(word1)
                    else:
                        return False
                word = []
        return True