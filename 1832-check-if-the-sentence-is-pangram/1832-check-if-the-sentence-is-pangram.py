class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alf = [False]  * 26
        for ch in sentence:
            alf[ord(ch) - ord('a')] = True
        return False not in alf