class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        glass = [0, 0]
        alf = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        for i, ch in enumerate(s):
            if ch in alf:
                if (i + 1) * 2 > len(s):
                    glass[0] += 1
                else:
                    glass[1] += 1
        return glass[0] == glass[1]