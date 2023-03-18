class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        answer = 0
        count = 0
        for i in range(len(s) + 1):
            if i == len(s) or s[i] == " ":
                if count > 0:
                    answer = count
                count = 0
            else:
                count += 1
        return answer