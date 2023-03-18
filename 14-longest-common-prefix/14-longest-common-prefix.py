class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_word = max_word = strs[0]
        for i in strs:
            if i < min_word:
                min_word = i
            if i > max_word:
                max_word = i
        result = ""
        while len(min_word) > len(result) < len(max_word) and max_word[len(result)] == min_word[len(result)]:
            result += max_word[len(result)]
        return result