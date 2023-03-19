class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        word_s1 = defaultdict(int)
        word_s2 = defaultdict(int)
        for word in s1.split():
            word_s1[word] += 1
        for word in s2.split():
            word_s2[word] += 1
        ans = []
        for key, item in word_s1.items():
            if word_s2[key] == 0 and item == 1:
                ans.append(key)
        for key, item in word_s2.items():
            if word_s1[key] == 0 and item == 1:
                ans.append(key)      
        return ans