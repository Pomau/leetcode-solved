class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans = 0
        people.sort()
        l = 0
        r = len(people) -1
        while r >= l:
            if people[r] + people[l] <= limit:
                l += 1
            r -= 1
            ans += 1
        return ans
                