class Solution:
    def countPoints(self, rings: str) -> int:
        alf = [[0] * 3 for i in range(10)]
        color = ["R", "G", "B"]
        for i in range(0, len(rings), 2):
            alf[int(rings[i + 1])][color.index(rings[i])] += 1
        ans = 0
        for i in range(10):
            os = True
            for ind in range(len(color)):
                if alf[i][ind] == 0:
                    os = False
            if os:
                ans += 1
        return ans