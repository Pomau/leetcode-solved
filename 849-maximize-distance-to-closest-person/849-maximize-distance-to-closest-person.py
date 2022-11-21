class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        suffix = [len(seats)]
        for i in range(len(seats) - 1, -1, -1):
            if seats[i] == 1:
                suffix.append(1)
            else:
                suffix.append(suffix[-1] + 1)
        suffix.reverse()
        now = len(seats)
        answer = 0
        for i in range(len(seats)):
            if seats[i] == 1:
                now = 1
            else:
                now += 1
            answer = max(answer, min(now, suffix[i]))
        return answer - 1