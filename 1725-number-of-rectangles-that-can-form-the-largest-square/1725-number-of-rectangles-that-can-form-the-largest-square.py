class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        maxn = max(min(rect) for rect in rectangles)
        ans = sum(1 for rect in rectangles if min(rect) == maxn)
        return ans