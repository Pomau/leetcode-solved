class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        used = set()
        count = 0
        for candy in candyType:
            if candy not in used and count < len(candyType) // 2:
                count += 1
                used.add(candy)
        return count