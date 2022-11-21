class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        alf = defaultdict(int)
        for i in range(len(s)):
            alf[s[i]] = i
        answer = []
        r = 0
        prew = 0
        for l in range(len(s)):
            r = max(r, alf[s[l]])
            if r == l:
                answer.append(r - prew + 1)
                prew = r + 1
        return answer