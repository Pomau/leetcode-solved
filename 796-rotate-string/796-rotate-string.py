class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        for i in range(len(s)):
            os = True
            for j in range(len(s)):
                now = (i + j) % len(s)
                if s[j] != goal[now]:
                    os = False
                    break
            if os:
                return True
        return False