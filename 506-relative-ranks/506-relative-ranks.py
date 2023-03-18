class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        scopes = []
        for i, scope in enumerate(score):
            scopes.append([scope, i])
        scopes.sort(reverse=True)
        answer = [""] * len(scopes)
        rank = ["Gold Medal","Silver Medal","Bronze Medal"]
        for i, scope in enumerate(scopes):
            if i < len(rank):
                answer[scope[1]] = rank[i]
            else:
                 answer[scope[1]] = str(i + 1)
        return answer