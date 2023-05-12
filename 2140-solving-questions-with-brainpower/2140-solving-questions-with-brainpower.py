class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        suffix = [0]
        for i in range(len(questions) - 1, -1, -1):
            suffix.append(max(suffix[-1], questions[i][0] + suffix[max(len(suffix) - questions[i][1] - 1, 0)]))
        # print(suffix)
        return suffix[-1]
        