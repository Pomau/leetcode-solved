class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        answer = []
        r1 = float("inf")
        r2 = 0
        answer = []
        while r2 < len(s) and s[r2] != c:
            r2 += 1
        for l in range(len(s)):
            if l > r2:
                r1 = r2
                r2 = l
                while r2 < len(s) and s[r2] != c:
                    r2 += 1
                if r2 >= len(s):
                    r2 = float("inf")
            answer.append(min(abs(r2 - l), abs(r1 - l)))
        return answer