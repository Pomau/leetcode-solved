class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i, flow in enumerate(flowerbed):
            if flow == 0 and (i > 0 and flowerbed[i - 1] == 0 or i == 0) and (i + 1 < len(flowerbed) and flowerbed[i + 1] == 0 or i + 1 == len(flowerbed)):
                n -= 1
                flowerbed[i] = 1
        return n <= 0