class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxk = max(candies)
        ans = []
        for i in range(len(candies)):
            ans.append(maxk <= candies[i] + extraCandies)
        return ans