class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        alf = defaultdict(int)
        for i, ch in enumerate(text):
            alf[ch] += 1
        target = "balloon"
        ans = float("inf")
        target_alf = defaultdict(int)
        for i, ch in enumerate(target):
            target_alf[ch] += 1
        for key, val in target_alf.items():
            ans = min(ans, alf[key] // val)
        return ans