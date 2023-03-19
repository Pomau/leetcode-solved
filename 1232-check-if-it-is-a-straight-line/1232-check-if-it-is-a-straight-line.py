class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        koef = None
        for i in range(2, len(coordinates)):
            if not self.check(coordinates[0], coordinates[1], coordinates[i]):
                return False
        return True
    def check(self, coord1, coord2, coord3):
        x = (coord3[0] - coord1[0]) *  (coord2[1] - coord1[1]) 
        y = (coord3[1] - coord1[1]) * (coord2[0] - coord1[0])
        return x == y