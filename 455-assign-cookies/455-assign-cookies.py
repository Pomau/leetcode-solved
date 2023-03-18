class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        r1 = len(g) - 1
        r2 = len(s) - 1
        g.sort()
        s.sort()
        answer = 0
        while r1 >= 0 and r2 >= 0:
            if g[r1] > s[r2]:
                r1 -= 1
            else:
                answer += 1
                r1 -= 1
                r2 -= 1
        return answer