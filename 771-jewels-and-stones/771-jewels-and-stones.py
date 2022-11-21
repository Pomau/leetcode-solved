class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set()
        for jewel in jewels:
            jewels_set.add(jewel)
        answer = 0
        for stone in stones:
            if stone in jewels_set:
                answer += 1
        return answer