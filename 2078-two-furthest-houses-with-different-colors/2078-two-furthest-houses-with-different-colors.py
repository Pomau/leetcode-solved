class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        used = set()
        ans = 0
        for i in range(len(colors)):
            if colors[i] in used:
                continue
            used.add(colors[i])
            for j in range(len(colors) -1, -1, -1):
                if colors[j] != colors[i]:
                    ans = max(ans, j - i)
                    break
            if len(used) == 2:
                break
        return ans