class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        dx = [0, 1, 1, -1, -1]
        dy = [1, 0, 1, 0, 1]
        pole = [[-1] * 3 for _ in range(3)]
        player = 1
        for move in moves:
            pole[move[0]][move[1]] = player
            status = False
            for i in range(3):
                for j in range(3):
                    if pole[i][j] == -1:
                        continue
                    for k in range(len(dx)):
                        x, y, = i, j
                        now = 0
                        while 0 <= x < 3 and 0 <= y < 3:
                            if pole[x][y] == pole[i][j]:
                                now += 1
                            else:
                                break
                            x += dx[k]
                            y += dy[k]
                        if now == 3:
                            if pole[i][j] == 1:
                                return "A"
                            else:
                                return "B"
            player = 1 - player
        print(pole)
        for i in range(3):
            for j in range(3):
                if pole[i][j] == -1:
                    return "Pending"
        return "Draw"
            