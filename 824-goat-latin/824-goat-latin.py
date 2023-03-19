class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        answer = []
        word = []
        for r, ch in enumerate(sentence):
            if ch.isalpha():
                word.append(ch)
            if (not ch.isalpha() or r + 1 == len(sentence)) and len(word) > 0:
                if word[0].lower() not in ['a', 'e', 'i', 'o', 'u']:
                    word.append(word[0])
                    word.remove(word[0])
                word.append("ma")
                word.append("a" * (len(answer) + 1))
                answer.append("".join(word))
                word = []
        return " ".join(answer)