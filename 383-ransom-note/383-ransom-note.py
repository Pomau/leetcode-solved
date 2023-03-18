class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        alf = defaultdict(int)
        for ch in magazine:
            alf[ch] += 1
        for ch in ransomNote:
            alf[ch] -= 1
            if alf[ch] < 0:
                return False
        return True