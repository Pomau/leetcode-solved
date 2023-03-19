class Solution:
    def countLargestGroup(self, n: int) -> int:
        alf = [0 for _ in range(100)] 
        for i in range(1, n + 1):
            now = 0
            num = i
            while num > 0:
                now += num % 10
                num //= 10
            alf[now] += 1
        maxk = 0
        ans = 0
        for i in range(len(alf)):
            if alf[i] > maxk:
                maxk = alf[i]
                ans = 0
            if alf[i] == maxk:
                ans += 1
        return ans
        