class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(reverse=True, key= lambda x: x[1])
        ans = 0
        for i in range(len(boxTypes)):
            k = min(boxTypes[i][0], truckSize)
            ans += k * boxTypes[i][1]
            truckSize -= k
        return ans