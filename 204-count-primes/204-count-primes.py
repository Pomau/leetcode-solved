class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [True] * n
        for a in range(2, int(n ** 0.5) + 1):
            if primes[a]:
                for b in range(a + a, n, a):
                    primes[b] = False
        return max(sum(primes) - 2, 0)
                