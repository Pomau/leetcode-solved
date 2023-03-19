class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alf = defaultdict(int)
        for i, ch in enumerate(order):
            alf[ch] = i
        for i, word in enumerate(words):
            if i == 0:
                continue
            word_l = words[i - 1]
            low = False
            for l in range(min(len(word), len(word_l))):
                if word[l] == word_l[l]:
                    continue
                if alf[word_l[l]] > alf[word[l]]:
                    return False
                else:
                    low = True
                    break
            if not low:
                if len(word) < len(word_l):
                    return False
        return True
