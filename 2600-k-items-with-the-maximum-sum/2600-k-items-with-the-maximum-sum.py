class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        ans = 0
        ans = min(k, numOnes)
        k -= numOnes
        if k > 0:
            k -= numZeros
        if k > 0:
            ans -= min(k, numNegOnes)
        return ans