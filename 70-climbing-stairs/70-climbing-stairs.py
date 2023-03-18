class Solution:
    def climbStairs(self, n: int) -> int:
        db  = [0] * (n  + 1)
        db[0] = 1
        for i in range(1, n + 1):
            db[i] = db[i - 1]
            if i > 1:
                db[i] += db[i - 2]
        return db[-1]
                