class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = [0]
        for i in range(1, n + 1):
            answer.append(i % 2 + answer[i // 2])
        return answer