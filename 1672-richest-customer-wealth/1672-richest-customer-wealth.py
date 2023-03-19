class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        answer = 0
        for acc in accounts:
            answer = max(answer, sum(acc))
        return answer