class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        alf = defaultdict(int)
        for i in range(lowLimit, highLimit + 1):
            now = 0
            for ch in str(i):
                now = now + int(ch)
            alf[now] += 1
        maxn = 0
        for key, item in alf.items():
            maxn = max(item, maxn)
        return maxn