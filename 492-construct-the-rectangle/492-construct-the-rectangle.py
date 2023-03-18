class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        ans = [0, 0]
        l = 1
        while l * l <= area:
            if area % l == 0:
                ans = [area // l, l]
            l += 1
        return ans