class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        mink = 0
        alf = defaultdict(int)
        for i, ch in enumerate(chars):
            alf[ch] = vals[i]
        ans = 0
        sums = 0
        for i, ch in enumerate(s):
            ves = ord(ch) - ord("a") + 1
            if ch in alf:
                ves = alf[ch]
            sums += ves
            ans = max(ans, sums - mink)
            mink = min(mink, sums)
        return ans
                