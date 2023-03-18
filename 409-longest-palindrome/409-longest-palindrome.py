class Solution:
    def longestPalindrome(self, s: str) -> int:
        alf = defaultdict(int)
        for ch in s:
            alf[ch] += 1
        count = 0
        center = False
        for key, value in alf.items():
            count += value - (value % 2)
            if not center and value % 2 == 1:
                count += 1
                center = True
        return count
