class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.image = image
        if image[sr][sc] != color:
            self.dfs(sr, sc, image[sr][sc], color)
        return self.image
    
    def dfs(self,x, y, last_color, new_color):
        if 0 <= x < len(self.image) and 0 <= y < len(self.image[0]) and self.image[x][y] == last_color:
            self.image[x][y] = new_color
            dx = [0 ,0, 1, -1]
            dy = [1, -1, 0, 0]
            for k in range(len(dx)):
                self.dfs(x + dx[k], y + dy[k], last_color, new_color)
