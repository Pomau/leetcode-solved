class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x, y = 0, 0
        turn = {
            "U": [1, 0],
            "D": [-1, 0],
            "R": [0, 1],
            "L": [0, -1]
        }
        for ch in moves:
            x += turn[ch][0]
            y += turn[ch][1]
        return x == y == 0