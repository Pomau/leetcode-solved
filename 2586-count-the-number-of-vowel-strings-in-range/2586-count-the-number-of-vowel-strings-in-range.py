class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        ut = ['a', 'e', 'i', 'o', 'u']
        count = 0
        for i in range(left, right + 1):
            if words[i][0] in ut and words[i][-1] in ut:
                count += 1
        return count