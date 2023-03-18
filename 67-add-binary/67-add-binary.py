class Solution:
    def addBinary(self, a: str, b: str) -> str:
        r1 = len(a) - 1
        r2 = len(b) - 1
        answer = []
        transfer = 0
        while r1 > -1 or r2 > -1 or transfer > 0:
            if r1 > -1:
                transfer += int(a[r1])
                r1 -= 1
            if r2 > -1:
                transfer += int(b[r2])
                r2 -= 1
            answer.append(str(transfer%2))
            transfer //= 2
        answer.reverse()
        return "".join(answer)