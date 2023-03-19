class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        ans = 0
        alf = defaultdict(int)
        for i in dominoes:
            a, b = i[0], i[1]
            if a < b:
                b, a = a, b
            word = f"{a}^{b}"
            ans += alf[word]
            alf[word] += 1
        return ans