class Solution:
    def isPathCrossing(self, path: str) -> bool:
        napr = {
            "N": [1, 0],
            "S": [-1, 0],
            "E": [0, 1],
            "W": [0, -1]
        }
        used = set()
        x, y = 0, 0
        for ch in path:
            used.add((x, y))
            x += napr[ch][0]
            y += napr[ch][1]
            if (x, y) in used:
                return  True
        return False