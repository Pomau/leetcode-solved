class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        coord = ord(coordinates[0]) - ord("a") + int(coordinates[1])
        return coord % 2 != 1