class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxk = max(candies)
        return [maxk <= candies[i] + extraCandies for i in range(len(candies))]