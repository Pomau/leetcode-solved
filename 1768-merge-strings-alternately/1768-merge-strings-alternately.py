class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = l2 = 0
        res = []
        order = True
        while l1 < len(word1) and l2 < len(word2):
            if order:
                res.append(word1[l1])
                l1 += 1
            else:
                res.append(word2[l2])
                l2 += 1
            order = not order
        if l1 < len(word1):
            res.append(word1[l1:])
        elif l2 < len(word2):
            res.append(word2[l2:])
        return ''.join(res)