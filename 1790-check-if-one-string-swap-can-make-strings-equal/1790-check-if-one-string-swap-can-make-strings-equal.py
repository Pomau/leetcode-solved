class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        changes = []
        for l in range(len(s1)):
            if s1[l] != s2[l]:
                changes.append(l)
        if len(changes) != 0:
            if not (len(changes) == 2 and s1[changes[0]] == s2[changes[1]] and s2[changes[0]] == s1[changes[1]]):
                return False
        return True