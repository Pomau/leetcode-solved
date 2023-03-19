class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = defaultdict(int)
        word = []
        maxk = ""
        for i, ch in enumerate(paragraph):
            if ch.isalpha():
                word.append(ch.lower())
            if (not ch.isalpha() or i == len(paragraph) - 1) and len(word) > 0:
                words["".join(word)] += 1
                if words[maxk] < words["".join(word)] and "".join(word) not in banned:
                    maxk = "".join(word)
                word = []
        return maxk
        