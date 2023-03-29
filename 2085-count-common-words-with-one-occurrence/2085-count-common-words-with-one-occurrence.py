class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        alf1 = defaultdict(int)
        alf2 = defaultdict(int)
        for word in words1:
            alf1[word] += 1
        for word in words2:
            alf2[word] += 1
        ans = 0
        for key, item in alf1.items():
            if item == 1 and alf2[key] == 1:
                ans += 1
        return ans