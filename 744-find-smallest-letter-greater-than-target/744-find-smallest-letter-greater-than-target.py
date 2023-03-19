class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = -1
        r = len(letters) - 1
        while r - l > 1:
            m = (r + l) // 2
            if letters[m] > target:
                r = m
            else:
                l = m
        if letters[r] <= target:
            r = 0
        return letters[r]