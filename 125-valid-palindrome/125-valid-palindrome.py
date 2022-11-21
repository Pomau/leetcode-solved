class Solution:
    def validCharacter(self, char):
        return char.isalpha() or char.isdigit()
    
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while r > l:
            while r >= 0 and not self.validCharacter(s[r]):
                r -= 1
            while l < len(s) and not self.validCharacter(s[l]):
                l += 1
            if r >= 0 and l < len(s):
                if s[l].lower() != s[r].lower():
                    return False
            r -= 1
            l += 1
        return True