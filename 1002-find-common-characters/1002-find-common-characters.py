class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        alf = defaultdict(int)
        for ch in words[0]:
            alf[ch] += 1
        for i in range(1, len(words)):
            now = defaultdict(int)
            for ch in words[i]:
                now[ch] += 1
            ans = defaultdict(int)
            for key, val in alf.items():
                ans[key] = min(val, now[key])
            alf = ans
        ans = []
        for key, val in alf.items():
            for i in range(val):
                ans.append(key)
        return ans
