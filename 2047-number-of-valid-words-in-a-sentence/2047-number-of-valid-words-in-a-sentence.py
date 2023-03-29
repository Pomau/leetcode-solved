class Solution:
    def countValidWords(self, sentence: str) -> int:
        ans = 0
        word = []
        os = True
        for i, ch in enumerate(sentence):
            if ch != " ":
                if ch.isdigit():
                    os = False
                if ch == "-" and not (len(word) > 0 and word[-1].isalpha()):
                    os = False
                word.append(ch)
            if (ch == " " or i + 1 == len(sentence)) and len(word) > 0:
                if word[-1] == "-" or word.count("-") > 1 or word.count("-") == 1 and not word[word.index("-") + 1].isalpha():
                    os = False
                cou = 0
                for k in ["!", ".", ","]:
                    cou += word.count(k)
                    if word.count(k) == 1 and word[-1] != k:
                        os = False
                    if cou > 1:
                        os = False
                if os:
                    ans += 1
                    print(word)
                os = True
                word = []
        return ans