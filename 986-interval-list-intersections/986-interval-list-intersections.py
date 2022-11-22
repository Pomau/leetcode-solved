class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        answer = []
        last = [-1, -1]
        l1 = l2 = 0
        while l1 < len(firstList) or l2 < len(secondList):
            now = [-1, -1]
            if l1 < len(firstList) and (l2 >= len(secondList) or firstList[l1][0] < secondList[l2][0]):
                now = firstList[l1]
                l1 += 1
            else:
                now = secondList[l2]
                l2 += 1
            if now[0] <= last[1]:
                answer.append([now[0], min(now[1], last[1])])
            last = [now[0], max(now[1], last[1])]
        return answer
                