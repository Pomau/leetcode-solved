class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        l = 0
        for i, ch in enumerate(name):
            if l >= len(typed):
                return False
            if ch != typed[l]:
                if i > 0 and typed[l] == name[i - 1]:
                    l += 1
                    while l < len(typed) and typed[l - 1] == typed[l]:
                        l += 1
                else:
                    return False
            if l < len(typed) and ch == typed[l]:
                l += 1
            else:
                return False
        while l < len(typed) and typed[l] == typed[l - 1]:
            l += 1
        return l >= len(typed)