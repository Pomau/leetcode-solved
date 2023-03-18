class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        ans = [[0] * len(img[0]) for _ in range(len(img))]
        dx = [0, 0, 0, 1, 1, 1, -1, -1, -1]
        dy = [1, -1, 0, 1, -1, 0, 1, -1, 0]
        for x in range(len(img)):
            for y in range(len(img[0])):
                count = 0
                sums = 0
                for k in range(len(dx)):
                    x2 = x + dx[k]
                    y2 = y + dy[k]
                    if 0 <= x2 < len(img) and 0 <= y2 < len(img[0]):
                        count += 1
                        sums += img[x2][y2]
                ans[x][y] = sums//count 
        return ans
