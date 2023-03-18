class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.alf = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        if digits == "":
            return []
        return self.recursionCombinations(digits, "")
    
    def recursionCombinations(self, digits: str, now: str) -> List[str]:
        if len(digits) == 0:
            return [now[::-1]]
        combinations = []
        for char in self.alf[digits[-1]]:
            combinations += self.recursionCombinations(digits[:-1], now + char)
        return combinations
        
        