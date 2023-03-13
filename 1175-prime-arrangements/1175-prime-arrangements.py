class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        prime = 0
        for i in range(2, n + 1):
            j = 2
            os = True
            while j * j <=i:
                if i % j == 0:
                    os = False
                j += 1
            if os:
                prime += 1
        no_prime = n - prime
        ans = 1
        for i in range(2, prime+ 1):
            ans *= i
        for i in range(2, no_prime+ 1):
            ans *= i
        return ans % (10**9 + 7)