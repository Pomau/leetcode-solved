class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        l1 = len(s) - 1
        c1 = 0
        c2 = 0
        l2 = len(t) - 1
        while l1 >= 0 and l2 >= 0:
            while l1 >= 0 and s[l1] == "#":
                c1 += 1
                l1 -= 1
            while l2 >= 0 and t[l2] == "#":
                c2 += 1
                l2 -= 1
            if c1 == 0 and c2 == 0:
                if s[l1] == t[l2]:
                    l1 -= 1
                    l2 -= 1
                else:
                    return False
            else:
                if c1 > 0:
                    l1 -= 1
                    c1 -= 1
                if c2 > 0:
                    l2 -= 1
                    c2 -= 1
        while l1 >= 0 and (s[l1] == "#" or c1 > 0):
            if s[l1] == "#":
                c1 += 1
            else:
                c1 -= 1
            l1 -= 1
        while l2 >= 0 and (t[l2] == "#" or c2 > 0):
            if t[l2] == "#":
                c2 += 1
            else:
                c2 -= 1
            l2 -= 1
        if l1 >= 0 or l2 >= 0:
            return False
        return True

