class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        nch = [[0, 0]]
        ch = [[0, 0]]
        answer = 0
        for i, el in enumerate(arr):
            nch.append([ch[-1][0] + (ch[-1][1] + 1) * el, ch[-1][1] + 1])
            ch.append([nch[-2][0] + (nch[-2][1]) * el, nch[-2][1]])
            answer += nch[-1][0]
        return answer
